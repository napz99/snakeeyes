#author napz

def level_1():
    search = [

        {"name" : "3dcart", "strings" : ["<!--START: 3dcart stats-->", "<!--END: 3dcart stats-->"],  "header-value" : [{"set-cookie":"3dvisit"}] },
        
        {"name" : "Drupal", "strings" : ["block-views", "nodeblock", 'Drupal', 'misc/drupal.css','misc/drupal.js','modules/field/theme/field.css'], "header" : ["x-drupal-cache"] },
        
        {"name" : "WordPress", "strings" : ["/wp-content/themes", "/wp-content/uploads", '/wp-content/themes']},
        
        {"name" : "Joomla", "strings" : ["media/system/js", "plugins/system/", 'templates/protostar/js/template.js', 'misc/drupal.css','misc/drupal.js']},
        
        {"name" : "Typo3", "strings" : ["--TYPO3SEARCH_end--", "typo3temp/js_css_optimizer/", "/typo3temp/pics/"], "header" : [] },
        
        {"name" : "SilverStripe", "strings" : ["index.php/framework/thirdparty/jquery/", "themes/simple/javascript/script.js", "themes/simple/css/reset.css"]},
        
        {"name" : "Concrete5", "strings" : ["/concrete/images", "concrete/js/"], "regex" : ["(?<=/files)/[0-9]*/[0-9]*/[0-9]*"] },
        
        {"name" : "Moodle", "strings" : ["theme/image.php", "moodle-block_navigation-navigation", "theme/yui_combo.php"] },
        
        {"name" : "Tiki Wiki", "strings" : ['="tiki-login.php', '="tiki-remind_password.php'] },
        
        {"name" : "Magento", "strings" : ['skin/frontend', 'catalog/product/cache', 'mage/cookies.js'] },
        
        {"name" : "PmWiki", "strings" : ['/skins/monobook/', "class='wikilink'", '<a accesskey=', "<span class='commentout-pmwikiorg'>", "<!--PageLeftFmt-->"] },
        
        {"name" : "MediaWiki", "strings" : ["mediawiki.page.startup", "mediawiki.legacy.wikibits", '(["mediawiki.action.view.postEdit"', '"mediawiki.user"', "mw.config.set({"] },
        
        {"name" : "Zikula", "strings" : ["typeof(Zikula)", "Zikula.Config", "z-clearfix","func=display&amp;"] },
        
        {"name" : "XOOPS", "strings" : ['content="XOOPS"', 'name="xoops_redirect"', "<!-- RMV: added module header -->"] },
        
        {"name" : "Prestashop", "strings" : ["prestashop/css/", "window.am =", '<input type="hidden" name="orderway"', "<!-- MODULE Block cart -->"] },
        
        {"name" : "Processwire", "strings" : ["/site/assets/files", "/site/templates/", '/site/templates/styles'] },
        
        {"name" : "Pimcore", "strings" : ["pimcore_area_"] , "header" : ["x-pimcore-output-cache-tag","x-pimcore-output-cache-date"], "header-value" : [{"x-powered-by":"pimcore"}]},
        
        {"name" : "Cotonti", "strings" : ["tags/tpl/tags.css", "m=passrecover", 'href="users?m=register"', 'action="register?a=add"']},
        
        {"name" : "Contao", "strings" : ["tl_files/images/", "ce_text", 'tl_files/design/"', '<!-- indexer::continue -->']},
        
        {"name" : "CMS Made Simple", "strings" : ["/cmsms"]},
        
        {"name" : "Serendipity", "strings" : ["serendipity_entry_body", "serendipity_entry_author_Admin", "serendipity_entryFooter", "serendipityLeftSideBar", "serendipitySideBarContent"]},
        
        {"name" : "Web2py", "strings" : ["w2p", "web2py_ajax_init()"], "header-value" : [{"x-powered-by":"web2py"}, {"x-pow":"Wxx"}]}
    ]
    return search

def common_headers():
    headers = ["accept", "accept-charset", "accept-encoding", "accept-language", "accept-datetime",\
               "authorization", "cache-control", "connection", "cookie", "content-length", "content-md5", \
               "content-type", "date", "expect", "from", "host","if-match", "if-modified-since", "if-none-match", \
               "if-range", "if-unmodified-since", "max-forwards", "origin", "pragma", "proxy-authorization", \
               "range", "referer", "te", "user-agent", "upgrade", "via", "warning", "x-requested-with", \
               "dnt", "x-forwarded-for", "x-forwarded-proto", "front-end-https","x-att-deviceid", "x-wap-profile"\
               "proxy-connection", "access-control-allow-origin", "accept-ranges", "age", "allow", "cache-control",\
               "connection", "content-encoding", "content-language", "content-length", "content-location", "content-md5",\
               "content-disposition", "content-range", "content-type", "date", "etag", "expires", "last-modified", "link"\
               "p3p", "pragrma", "proxy-authenticate", "refresh", "retry-after", "status", "strict-transport-security", \
               "trailer", "transfer-encoding", "vary", "www-authenticate", "x-frame-options", "public-key-pins", "x-xss-protection",\
               "content-security-policy", "x-webkit-csp", "x-content-type-options"]
    return headers

def cms_list():
    cms = ["Drupal", "WordPress", "Joomla", "Typo3", "SilverStripe", "Concrete5", "Moodle", "Tiki Wiki", \
           "Magento", "PmWiki", "MediaWiki","Zikula", "XOOPS", "Prestashop", "ProcessWire", "Pimcore", "Cotonti","Contao",\
           "Jamroom", "CMS Made Simple", "Serendipity", "Web2py", "3dcart"]
    return cms

def common_cookies():
    cookies = ["domain_specified","path_specified", "secure", "expires", "discard", "comment", "comment_url", "_now"]
    return cookies