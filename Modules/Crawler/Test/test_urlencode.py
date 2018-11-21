# -*- coding: utf-8 -*-

#---------------------------------------
#   程序：test_urlencode.py
#   版本：0.1
#   作者：ctang
#   日期：2016-02-19
#   语言：Python 2.7.10
#   说明：测试urlencode方法
#---------------------------------------

import urllib
import urllib2

data = {}
data['word'] = 'python'

url_value = urllib.urlencode(data)
url = "http://www.baidu.com/s?"
full_url = url + url_value
print full_url

page = urllib2.urlopen(full_url).read()
result = page.decode('utf-8')
print result

