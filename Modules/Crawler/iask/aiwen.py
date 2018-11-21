# -*- coding: utf-8 -*-

#---------------------------------------
#   程序：aiwen.py
#   版本：0.1
#   作者：ctang
#   日期：2016-02-18
#   语言：Python 2.7.10
#   说明：爬取新浪爱问知识人的问题列表
#---------------------------------------

import urllib2
import time
import sys
import re
from HttpClient import HttpClient
from bs4 import BeautifulSoup
import types

#解决以下问题
#Error 'ascii' codec can't encode characters in position 0-1: ordinal not in range(128)
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)

class AiWen(HttpClient):
    def __init__(self):
        self.__iaskUrl = "http://iask.sina.com.cn"
        self.__url = "http://iask.sina.com.cn/c/978-all-"
        self.__refer = "http://iask.sina.com.cn/c/978-all-1.html"

    def __getMaxPage(self):
        page = self.Get(self.__refer)
        pattern_maxPage = re.compile('<div.*?id="pagesHolder".*?pageCount="(.*?)".*?>')
        maxPage = re.search(pattern_maxPage, page).group(1)
        #print type(maxPage) #<type 'str'>
        return int(maxPage)

    #获取当前时间
    def __getCurrentTime(self):
        return time.strftime('[%Y-%m-%d %H:%M:%S]', time.localtime(time.time()))

    #获取当前日期
    def __getCurrentDate(self):
        return time.strftime('%y-%m-%d', time.localtime(time.time()))

    #获取第pageIndex个网页的问题汇总
    def __getQuestionsByPageIndex(self, pageIndex):
        realUrl = self.__url + str(pageIndex) + ".html"
        #print realUrl
        print self.__getCurrentTime() + " 正在爬取第" + str(pageIndex) + "页数据~"
        page = self.Get(realUrl)
        pattern_questionItem = re.compile('<div.*?class="question_item">.*?<ul.*?class="question_li">(.*?)</ul>', re.S)
        questionItem = re.search(pattern_questionItem, page).group(1)
        #print questionItem
        pattern_questionLi = re.compile('<li>(.*?)</li>', re.S)
        questionLi = re.findall(pattern_questionLi, questionItem)
        for questionList in questionLi:
            #print questionList
            pattern_question = re.compile('<a.*? href="(.*?)".*?>(.*?)</a>.*?<span.*?class=".*?answer_num.*?">(.*?)</span>', re.S)
            question = re.search(pattern_question, questionList)
            #print self.__iaskUrl + question.group(1) + " " + question.group(2) + " " + question.group(3)
            pattern_answerNum = re.compile('[0-9]+')
            answerNum = re.search(pattern_answerNum, question.group(3)).group()
            print self.__getCurrentTime() + " 发现问题：" + question.group(2) + ",回答数量 " + str(answerNum)
            if answerNum != 0:
                self.__getQuestionDetails(self.__iaskUrl + question.group(1))

    #获取问题的详细信息
    def __getQuestionDetails(self, url):
        page = self.Get(url)
        soup = BeautifulSoup(page, "html.parser")
        answers = soup.find_all(attrs={"class":"answer_txt"})
        answerNumber = 1
        for answer in answers:
            #print type(answer)
            #print type(answer.span.pre.string)
            if type(answer.span.pre.string) is not types.NoneType:
                try:
                    print u"回答" + str(answerNumber) + u":" + answer.span.pre.string
                except Exception, e:
                    print "Error", e
            else:
                #print answer
                pattern_answerCombine = re.compile(r'<pre.*?>(.*?)<div.*?target="_blank">(.*?)</a>.*?</div></div></div>(.*?)</pre>', re.S)
                answerCombine = re.search(pattern_answerCombine, str(answer))
                try:
                    print u"回答" + str(answerNumber) + u":" + answerCombine.group(1).strip().decode('utf-8', 'ignore') + answerCombine.group(2).strip().decode('utf-8', 'ignore') + answerCombine.group(3).strip().decode('utf-8', 'ignore')
                except Exception, e:
                    print "Error", e

            answerNumber = answerNumber+1

    def start(self):
        #输出到日志
        #f_handler = open('out.log', 'w')
        #sys.stdout = f_handler
        #maxPage = self.__getMaxPage()
        maxPage = 2
        for i in range(1, maxPage+1):
            self.__getQuestionsByPageIndex(i)

aiwen = AiWen()
aiwen.start()





