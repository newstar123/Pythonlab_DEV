# -*- coding: utf-8 -*-

#---------------------------------------
#   程序：test_headers.py
#   版本：0.1
#   作者：ctang
#   日期：2016-02-22
#   语言：Python 2.7.10
#   说明：伪装浏览器
#---------------------------------------

# Method 1
# 方法比较简单直接，但是不好扩展功能
'''
import urllib2

url = 'http://www.baidu.com'
req = urllib2.Request(url, headers={
    'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
})
opener = urllib2.urlopen(req)
data = opener.read()
print data.decode('utf-8')
'''

# Method 2
# 使用build_opener方法，用来自定义opener，这种方法的好处是可以方便的拓展功能。
import urllib2
import cookielib

def makeMyOpener():
    head = {
        'Connection': 'Keep-Alive',
        'Accept': 'text/html, application/xhtml+xml, */*',
        'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
    }
    cookie = cookielib.CookieJar()
    handler = urllib2.HTTPCookieProcessor(cookie)
    opener = urllib2.build_opener(handler)
    header = []
    for key, value in head.items():
        elem = (key, value)
        header.append(elem)
    opener.addheaders = header
    return opener

opener = makeMyOpener()
uop = opener.open('http://www.baidu.com', timeout = 1000)
data = uop.read()
print data.decode('utf-8')

