# -*- coding: utf-8 -*-

#---------------------------------------
#   程序：smzdm.py
#   版本：0.1
#   作者：ctang
#   日期：2016-01-29
#   语言：Python 2.7.10
#   说明：爬取前5页什么值得买(http://www.smzdm.com/)网站中的白菜价包邮信息。包括名称，价格。
#---------------------------------------

import re
from HttpClient import HttpClient

#Smzdm类是HttpClient类的子类
class Smzdm(HttpClient):
    def __init__(self):
        self.__Url = 'http://faxian.smzdm.com/9kuai9/p'

    #正则得到每页商品信息
    def __getAllGoods(self, pageIndex):
        realUrl = self.__Url + str(pageIndex)
        pageCode = self.Get(realUrl)
        pattern = re.compile('<h2.*?itemName"><a.*?class="black">(.*?)</span>.*?class="red">(.*?)</span>', re.S)
        result = re.findall(pattern, pageCode.decode('utf-8'))
        for item in result:
            print item[0], item[1]

    def start(self):
        for i in range(1, 6):
            print u"正在获取第" + str(i) + u"页数据..."
            self.__getAllGoods(i)

smzdm = Smzdm()
smzdm.start()


