# -*- coding: utf-8 -*-

#---------------------------------------
#   程序：jandan.py
#   版本：0.1
#   作者：ctang
#   日期：2016-02-01
#   语言：Python 2.7.10
#   说明：爬取jandan.net网站妹子图
#---------------------------------------

#避免在中文前面加u，以考虑到迁移到python3
from __future__ import unicode_literals
import os
import re
from HttpClient import HttpClient

class JanDan(HttpClient):
    def __init__(self):
        self.__pageIndex = 1500 #page 1500之前的图片被归档了
        self.__Url = 'http://jandan.net/ooxx/'
        self.__folder = 'jandan'

    def __getAllPicUrl(self,pageIndex):
        realUrl = self.__Url + "page-" + str(pageIndex) + "#comments"
        print "目标地址：" + realUrl
        page = self.Get(realUrl)
        pattern = re.compile('<div class="row">.*?<p><a.*?href="(.*?)"', re.S)
        result = re.findall(pattern, page.decode('utf-8'))
        for item in result:
            print "发现图片" + item
            self.__savePics(item)

    def __savePics(self, img_addr):

        picName = img_addr.split('/')[-1]
        fileName = self.__folder + '/' + picName
        print "正在保存" + picName
        #self.Download(img_addr, fileName)
        with open(fileName,'wb') as file:
            img = self.Get(img_addr)
            file.write(img)

    def __getNewPage(self):
        page = self.Get(self.__Url)
        pattern = re.compile(r'<div .*?cp-pagenavi">.*?<span .*?current-comment-page">\[(.*?)\]</span>', re.S)
        result = re.search(pattern, page)
        if result != None:
            newestPage = result.group(1)
        return newestPage

    def start(self):
        if not os.path.exists(self.__folder):
            os.mkdir(self.__folder)
        page = int(self.__getNewPage())
        for i in range(self.__pageIndex, page):
            self.__getAllPicUrl(i)


if __name__ == '__main__':
    jd = JanDan()
    jd.start()

