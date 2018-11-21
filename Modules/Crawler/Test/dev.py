# -*- coding: utf-8 -*-

#---------------------------------------
#   程序：dev.py
#   版本：0.1
#   作者：ctang
#   日期：2016-01-29
#   语言：Python 2.7.10
#   说明：开发测试用
#---------------------------------------

import urllib2

url = 'http://news.dbanotes.net'
#url = 'http://ww2.sinaimg.cn/large/6a195423jw1ezxulzbeu2j20iq0ggt9y.jpg'

urlop = urllib2.urlopen(url)

print dir(urlop)
print "#" * 40

print urlop.headers
print "#" * 40

info = urlop.info()
for key in info:
    print '%s: %s' % (key, info[key])
print "#" * 40

print info['content-type']
