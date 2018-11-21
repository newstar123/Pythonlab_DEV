# -*- coding: utf-8 -*-

#---------------------------------------
#   程序：test_cookie.py
#   版本：0.1
#   作者：ctang
#   日期：2016-01-29
#   语言：Python 2.7.10
#   说明：测试cookie
#---------------------------------------

import urllib2
import cookielib

#声明一个CookieJar对象实例来保存cookie
cookie = cookielib.CookieJar()

#利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
handler = urllib2.HTTPCookieProcessor(cookie)

#通过handler来构建opener
opener = urllib2.build_opener(handler)

#此处的open方法同urllib2的urlopen方法，也可以传入request
response = opener.open('http://www.baidu.com')
for item in cookie:
    print 'Name = ' + item.name
    print 'Value = ' + item.value

#利用cookie请求访问另一个网址
gradeUrl = 'http://baike.baidu.com/link?url=XA3yxDlwVM5VKb56OjuPNuC6IB5uomYRy7U7XsmhMsK8tMwWxNZcFnj8oAsv-hdwT5ve6bBmwEwNmSythtNyFK'

#请求访问
result = opener.open(gradeUrl)
print result.read()


