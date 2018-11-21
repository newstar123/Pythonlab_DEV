# -*- coding: utf-8 -*-

#---------------------------------------
#   程序：get_cnblogs_info.py
#   版本：0.1
#   作者：ctang
#   日期：2016-03-02
#   语言：Python 2.7.10
#   说明：获取cnblogs信息并存入数据库
#---------------------------------------

import sys
import urllib2
import re
from DBUtil import MySQL

default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)

# 数据库连接参数
dbconfig = {'host':'localhost',
            'port': 3306,
            'user':'root',
            'passwd':'abc123',
            'db':'pythonlab',
            'charset':'utf8'}

# 连接数据库，创建这个类的实例
db = MySQL(dbconfig)

def insertData(table, myDict):
    cols = ', '.join(myDict.keys())
    values = '"," '.join(myDict.values())
    sql = "INSERT INTO %s (%s) VALUES (%s)" % (table, cols, '"'+values+'"')
    #print sql
    result = db.insert(sql)
    print result

table = "tbl_cnblogs_info"

for i in range(1, 9):
    indexUrl = 'http://www.cnblogs.com/mchina/default.html?page=%s' % i
    page = urllib2.urlopen(indexUrl)
    html = page.read()

    pattern_blogs = re.compile(r'<a.*?class="postTitle2".*?href="(.*?)">(.*?)</a>.*?class="c_b_p_desc">(.*?)<a.*?class="postDesc">(.*?)<a.*?', re.S)
    blogs = re.findall(pattern_blogs, html)
    for item in blogs:
        #print item[0] + "\n" + item[1] + "\n" + item[2] + "\n" + item[3]
        postDesc = item[3].strip().decode('utf-8')
        postDescList = postDesc.split()
        blog_post_time = postDescList[2] + " " + postDescList[3]
        blog_page_views = postDescList[5][:-1][3:]
        blog_commentcount = postDescList[6][:-1][3:]

        blog_dict = {
            "blog_title": item[1],
            "blog_desc": item[2],
            "blog_url": item[0],
            "blog_post_time": blog_post_time,
            "blog_page_views": blog_page_views,
            "blog_commentcount": blog_commentcount
        }

        insertData(table, blog_dict)
