# -*- coding: utf-8 -*-

#---------------------------------------
#   程序：test_login.py
#   版本：0.1
#   作者：ctang
#   日期：2016-02-24
#   语言：Python 2.7.10
#   说明：测试简单的登录动作
#---------------------------------------

import urllib
import urllib2
import cookielib
import gzip

def ungzip(data):
    try:
        print "正在解压......"
        data = gzip.decompress(data)
        print "解压完毕！"
    except:
        print "未经压缩，无需解压！"
    return data

def getOpener(head):
    cookie = cookielib.CookieJar()
    handler = urllib2.HTTPCookieProcessor(cookie)
    opener = urllib2.build_opener(handler)
    header = []
    for key, value in head.items():
        elem = (key, value)
        header.append(elem)
    opener.addheaders = header
    return opener

header = {
    'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Host': '6.thinkshare.sinaapp.com',
}

url = 'http://6.thinkshare.sinaapp.com/manage/mis.php?action=login'
username = 'admin'
password = 'abc123'
postDict = {
    'username': username,
    'password': password
}

opener = getOpener(header)
postData = urllib.urlencode(postDict)
op = opener.open(url, postData)
data = op.read()
data = ungzip(data)

print data
