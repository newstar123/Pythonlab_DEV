# -*- coding: utf-8 -*-

#---------------------------------------
#   程序：rosi.py
#   版本：0.1
#   作者：ctang
#   日期：2016-02-15
#   语言：Python 2.7.10
#   说明：爬取http://www.5442.com/tag/fengguang/网站风光图
#   参考：http://www.cnblogs.com/jixin/p/5144333.html
#---------------------------------------

from __future__ import unicode_literals
from HttpClient import HttpClient
import re,sys,os
from threading import Thread
from Queue import Queue

#图片集url队列
q = Queue()

#一级url爬取类
class GetRosiUrl(HttpClient):
    def __init__(self):
        self.__pageIndex = 1
        self.__Url = "http://www.5442.com/tag/shaonv/"
        self.__refer = "http://www.5442.com/tag/shaonv.html"

    #将爬取的图片集url放入队列
    def __getAllPicUrl(self, pageIndex):
        realUrl = self.__Url + str(pageIndex) + ".html"
        print realUrl
        page = self.Get(realUrl, self.__refer)
        type = sys.getfilesystemencoding()
        pattern = re.compile(r'<div.*?title">.*?<span><a href="(.*?)".*?</a>', re.S)
        result = re.findall(pattern, page.decode("gbk",'ignore').encode(type))
        for item in result:
            #print item
            global q
            q.put(item)
            #print "放入队列"

    #得到最新页码
    def __getNewestPage(self):
        page = self.Get(self.__refer)
        pattern_ul = re.compile(r'<ul.*?<li.*?pageinfo">(.*?)</li>', re.S)
        ul_result = re.search(pattern_ul, page.decode('gbk'))
        pattern_page = re.compile('[0-9]+')
        pageInfo = re.search(pattern_page, ul_result.group(1).split("/")[0])
        num = pageInfo.group()
        if ul_result != None:
            return int(num)
        return 0

    def start(self):
        page = self.__getNewestPage()
        for i in range(1, page+1):
            self.__getAllPicUrl(i)

#图片下载类
class DownloadImg(HttpClient):
    def __init__(self):
        self.__refer = "http://www.5442.com/tag/shaonv.html"

    #获取二级url的最大页码
    def __getMaxPage(self):
        page = self.Get(self.__Url, self.__refer)
        pattern_ul = re.compile(r'<ul.*?<li>.*?<a>(.*?)</a></li>', re.S)
        ul_result = re.search(pattern_ul, page.decode('gbk', 'ignore'))
        pattern_page = re.compile('[0-9]+')
        pageInfo = re.search(pattern_page, ul_result.group(1))
        num = pageInfo.group()
        if ul_result != None:
            return int(num)
        return 0

    #得到图片集名称
    def __getBookName(self):
        page = self.Get(self.__Url, self.__refer)
        type = sys.getfilesystemencoding()
        pattern = re.compile(r'<h1><a.*?>(.*?)</a></h1>', re.S)
        result = re.search(pattern, page.decode('gbk', 'ignore').encode(type))
        if result != None:
            return result.group(1)
        return "未命名"

    #得到每页图片url
    def __getAllPicUrl(self, pageIndex):
        if pageIndex == 1:
            realUrl = self.__Url
        else:
            realUrl = self.__Url[:-5] + "_" + str(pageIndex) + ".html"
        #print realUrl
        page = self.Get(realUrl)
        pattern_contents = re.compile('<p align="center".*?>(.*?)</p>', re.S)
        imgs = re.search(pattern_contents, page.decode('gbk', 'ignore')).group(1)
        pattern_img = re.compile('<a href=(.*?) title=.*?>')
        result = re.findall(pattern_img, imgs)
        self.__savePics(result, self.__folder)

    #下载保存图片
    def __savePics(self, img_addr, folder):
        for item in img_addr:
            realUrl = item.split('?')[-1][:-1]
            filename = self.__folder + "\\" + item.split('/')[-1][:-1]
            if not os.path.exists(filename):
                print "正在保存图片：" + filename
                print realUrl
                with open(filename, 'wb') as file:
                    img = self.Get(realUrl)
                    file.write(img)
            else:
                print filename + "已存在~"

    def start(self):
        while True:
            global q
            #从队列中取出一条图片集Url
            self.__Url = q.get()
            #获取图片集名称
            title = self.__getBookName()
            #创建与图片集名称相同的子目录
            self.__folder = os.getcwd() + "\\shaonv\\" + title.decode("gbk", 'ignore')
            if not os.path.exists(self.__folder):
                os.mkdir(self.__folder)

            page = self.__getMaxPage() + 1
            for i in range(1, page):
                self.__getAllPicUrl(i)

            q.task_done()


if __name__ == '__main__':
    if not os.path.exists("shaonv"):
        os.mkdir("shaonv")
    #新建5个线程 等待队列
    '''
    for i in range(2):
        downImg = DownloadImg()
        t = Thread(target=downImg.start)
        t.start()
    '''
    rosi = GetRosiUrl()
    rosi.start()
    downImg = DownloadImg()
    downImg.start()

    q.join


