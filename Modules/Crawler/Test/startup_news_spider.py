# -*- coding: utf-8 -*-

#---------------------------------------
#   程序：startup_news_spider.py
#   版本：0.1
#   作者：ctang
#   日期：2016-01-29
#   语言：Python 2.7.10
#   说明：Python网络爬虫Ver 1.0 alpha
#---------------------------------------

import sys
import re
import urllib2
from collections import deque

default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)

queue = deque()
visited = set()

#url = "http://news.dbanotes.net"    # 入口页面, 可以换成别的
url = "http://www.cnblogs.com/mchina/"

queue.append(url)
cnt = 0

while queue:
    print 'queue length: ' + str(len(queue)) + ",",
    url = queue.popleft()   # 队首元素出列
    visited |= {url}        # 标记为已访问

    print '已经抓取：' + str(cnt) + ', 正在抓取 -> ' + url
    cnt += 1
    try:
        urlop = urllib2.urlopen(url, timeout=2)
        if 'html' not in urlop.info()['content-type']:
            continue
    except Exception, e:
        print "Error", e

    try:
        data = urlop.read().decode('utf-8')
    except:
        continue

    linkre = re.compile(r'href="(.+?)"')
    for x in linkre.findall(data):
        if 'http' in x and x not in visited and x not in queue:
            queue.append(x)
            print '加入队列 -> ' + x

    #print "queue:" + str(queue)
    #print "队列：" + str(visited)
