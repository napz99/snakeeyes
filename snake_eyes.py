#author napz
import sys, requests
import reconlib
import re
from collections import Counter
from requests.packages.urllib3.connectionpool import HTTPConnectionPool
from bs4 import BeautifulSoup

class snake_eyes():

    def __init__(self, host, level=1):
        print "SnakeEyes Recon > started"
        self.level = level
        self.host = host
        self.ip_address = None
        self.score = {}
        for name in reconlib.cms_list():
            self.score[name] = {}
            self.score[name]['level 1'] = 0
            self.score[name]['level 2'] = 0
        print "Target : " + host

    def init_request(self):
        def _make_request(self, conn,method,url,**kwargs):
            response = self._old_make_request(conn,method,url,**kwargs)
            sock = getattr(conn,'sock',False)
            if sock:
                setattr(response,'peer',sock.getpeername())
            else:
                setattr(response,'peer',None)
            return response

        HTTPConnectionPool._old_make_request = HTTPConnectionPool._make_request
        HTTPConnectionPool._make_request = _make_request

        headers = {
            'User-Agent': 'SnakeEyes'
        }

        try:
            recon = requests.get(self.host, headers=headers, verify=False)
            if recon.raw._original_response.peer != None:
                self.ip_address = recon.raw._original_response.peer[0]
                print "IP :["+str(self.ip_address)+"]"
        except requests.exceptions.RequestException as e:
            print e
            sys.exit(1)
        return recon

    def recon(self):
        recon = self.init_request()
        if self.level >= 1:
            print "Performing level 1 scan :"
            self.level_1(recon)

    def level_1(self, recon):
        x = reconlib.level_1()

        for y in x:
            for search in y['strings']:
                if search in recon.content:
                    self.score[y['name']]['level 1'] = self.score[y['name']]['level 1'] + 40
                    if self.score[y['name']]['level 1'] >= 80:
                        break

        #regex search
        for y in x:
            if y.has_key("regex"):
                for search in y['regex']:
                    result = re.findall(search,recon.content)
                    if  len(result) > 0:
                        self.score[y['name']]['level 1'] = self.score[y['name']]['level 1'] + 40
                        break

        interesting_header = self.check_headers(recon.headers)
        interesting_cookies = self.check_cookies(recon.cookies.__dict__)

        if len(interesting_cookies) > 0:
            for cookie_value in interesting_cookies:
                print "Cookie :["+str(cookie_value)+"] | Value:["+str(interesting_cookies[cookie_value])+"]"
        #for header-value
        for y in x:
            if y.has_key("header-value"):
                header_check = set(y['header-value'][0].keys()).intersection(interesting_header.keys())
                if len(header_check) > 0:
                    header_check = list(header_check)
                    self.score[y['name']]['level 1'] = self.score[y['name']]['level 1'] + 40
        #for header only
        for header_value in interesting_header:
            print "Header :["+ str(header_value) +"] | Value:["+str(interesting_header[header_value])+"]"
            for y in x:
                if y.has_key("header"):
                    if  header_value in y['header']:
                        self.score[y['name']]['level 1'] = self.score[y['name']]['level 1'] + 40
                        break

        poweredby = self.poweredby(recon.content)
        if poweredby['name'] != None:
            print "PoweredBy :["+str(poweredby['name'])+"]"

        metacheck = self.metachecker(recon.content)
        if metacheck['score'] != 0:
            self.score[metacheck['name']]['level 1'] = self.score[metacheck['name']]['level 1'] + 40
            print "Meta Generator :[ "+str(metacheck['meta_value'])+" ]"

    def check_headers(self, request_header):
        headers = reconlib.common_headers()
        clean_header = set(request_header).intersection(headers)
        resultlist_header = list(clean_header)
        for value in resultlist_header:
            del request_header[value]
        return request_header

    def check_cookies(self, request_cookies):
        cookies = reconlib.common_cookies()
        clean_cookies = set(request_cookies).intersection(cookies)
        resultlist_cookies= list(clean_cookies)
        for value in resultlist_cookies:
            print value
            del request_cookies[value]
        return request_cookies

    def metachecker(self, response_content):
        recon_soup = BeautifulSoup(response_content)
        try:
            meta_value = recon_soup.find("meta",{"name":"generator"}).get("content")
        except:
            return {"name": None ,"score" : 0, "meta_value" : None}
        cms = reconlib.level_1()
        score = 0
        name = ""
        for cms_name in cms:
            if self.stringfinder(meta_value.lower(), cms_name['name'].lower()) == 1:
                score = 50
                name = cms_name['name']
                break
        return {"name": name ,"score" : score, "meta_value" : meta_value}

    def stringfinder(self, hay, needle):
        if hay.find(needle) >= 0:
            return 1
        else:
            return 0

    def poweredby(self, response_content):
        result = re.search('(?<=powered by )(<.*>+|[a-z]*)', response_content, re.IGNORECASE)
        try:
            power = result.group(0)
            for name in reconlib.cms_list():
                if self.stringfinder(power, name) == 1:
                    self.score[name]['level 1'] = self.score[name]['level 1'] + 40
                    break
            #print "foooo"
            if self.stringfinder(power, "<a"):
                x = BeautifulSoup(power)
                power = x.find_all("a")[0].text

            return {"name" : power}
        except:
            return {"name" : None}

    def certainty(self):
        x = Counter(self.score).most_common()
        if x[0][1]['level 1'] > 0:
            for y in x:
                if y[1]['level 1'] >=40:
                    print "--------------------------------"
                    print "Detected :[" + str(y[0]) +"]"
                    print "Level 1 of certainty: " + str(y[1]['level 1'])
                    print "Level 2 of certainty: " + str(y[1]['level 2'])
            #print "Detected :[" + str(x[0]) +"]"
            #print "Level 1 of certainty: " + str(x[1]['level 1'])
            #print "Level 2 of certainty: " + str(x[1]['level 2'])
        else:
            print "No CMS Detected"


if len(list(sys.argv)) == 2:
    target = sys.argv[1]
    snake = snake_eyes(target)
    snake.recon()
    snake.certainty()
else:
    print "target host not define"

