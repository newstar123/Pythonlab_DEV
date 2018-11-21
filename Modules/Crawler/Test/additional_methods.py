# -*- coding: utf-8 -*-

#---------------------------------------
#   程序：additional_methods.py
#   版本：0.1
#   作者：ctang
#   日期：2016-02-19
#   语言：Python 2.7.10
#   说明：获取urllib2.urlopen返回的三个额外方法的结果
#---------------------------------------

import urllib2

page = urllib2.urlopen("http://www.cnblogs.com/mchina/")
url = page.geturl()
info = page.info()
code = page.getcode()

print "URL: " + url
for key in info:
    print '%s: %s' % (key, info[key])
print "Code: " + str(code)






