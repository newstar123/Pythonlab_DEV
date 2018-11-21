# -*- coding: utf-8 -*-

#---------------------------------------
#   程序：内涵吧GIF趣图爬虫
#   版本：0.1
#   作者：ctang
#   日期：2016-01-28
#   语言：Python 2.7.10
#   说明：自定义下载页数
#---------------------------------------

import urllib2
import os
from bs4 import BeautifulSoup

page_num = 2    #设置下载页数

path = os.getcwd()
path = os.path.join(path, 'neihan8_GIF')
if not os.path.exists(path):
    os.mkdir(path)  #创建文件夹

url = "http://www.neihan8.com/gif/" #url地址
header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0'
}

def get_gif(url):
    req = urllib2.Request(url, headers=header)
    res = urllib2.urlopen(req).read()
    soup = BeautifulSoup(res, "html.parser")
    detail_content = soup.find(attrs={"class":"detail"})
    img = detail_content.find("img")
    return img.get("src")

number = 1
total = page_num * 28

for count in range(page_num):
    if count == 0:
        full_url = url + "index.html"
    else:
        full_url = url + "index_" + str(count+1) + ".html"

    #print full_url
    req = urllib2.Request(full_url, headers=header)
    res = urllib2.urlopen(req).read()
    soup = BeautifulSoup(res, "html.parser")
    #print soup
    div_content = soup.find(attrs={"class":"pic-column-list mt10"})
    #print div_content
    h3_content = div_content.find_all("h3")

    for h3 in h3_content:
        a_content = h3.find("a")
        link = a_content.get("href")
        link_add = "http://www.neihan8.com" + link
        a_string = a_content.string
        filename = path + os.sep + a_string + ".gif"
        gif_src = get_gif(link_add)
        req = urllib2.Request(gif_src, headers=header)
        data = urllib2.urlopen(req).read()
        f = open(filename, 'wb')
        f.write(data)
        print u"共" + str(total) + u"张," + u"正在获取第" + str(number) + u"张,", a_string, link_add, gif_src
        number += 1
        f.close()


