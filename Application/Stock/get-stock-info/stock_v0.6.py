#!/usr/bin/env python
# -*- coding: utf-8 -*-

#---------------------------------------
#   Program: stock_v0.6.py
#   Version: 0.6
#   Author: Alan Tang
#   Date: 2017-08-22
#   Language: Python 2.7.12
#   Description: 自动刷新
#---------------------------------------

from __future__ import print_function
import urllib2
from bs4 import BeautifulSoup
from prettytable import PrettyTable
import uniout
from xpinyin import Pinyin
import time

p = Pinyin()

stock_list = ['000001', '002689', '601628', '600326']

baseUrl = "https://gupiao.baidu.com/stock/"

while True:
    x = PrettyTable(["Stock Name", "Current Price", "Change", "Rate", "Max", "Min"])
    # x.align["Stock Name"] = "l"
    x.padding_width = 1

    for stock in stock_list:
        if stock.startswith('00') and stock != '000001':
            stockCode = 'sz'
        elif stock.startswith('60') or stock == '000001':
            stockCode = 'sh'

        full_url = baseUrl + stockCode + stock + '.html'
        # print(full_url)

        page = urllib2.urlopen(full_url)
        html = page.read()
        # print(html)

        soup = BeautifulSoup(html, 'html.parser')

        stockInfo = soup.find('div', attrs={'class':'stock-bets'})
        stockName = stockInfo.find_all(attrs={'class':'bets-name'})[0].text.split()[0]

        # 汉字转换成拼音
        stockName_pinyin = p.get_initials(stockName, u'')
        # print(stockName_pinyin)

        # print("Stock Name: %s" % stockName)

        price_class = soup.find('div', attrs={'class':'price'})
        # print(price_class)
        current_price = price_class.strong.string
        # print("Current Price: %s" % current_price)

        price_range = price_class.find_all('span')
        # for i in price_range:
        #     print(i.string)
        change_price = price_range[0].string
        change_rate = price_range[1].string
        # print("Change: %s" % change_price)
        # print("Rate: %s" % change_rate)

        infoDict = {}
        keyList = stockInfo.find_all('dt')
        valueList = stockInfo.find_all('dd')

        for i in range(len(keyList)):
            key = keyList[i].text
            val = valueList[i].text
            infoDict[key] = val

        # print(infoDict)
        max_price = infoDict.get(u'最高')
        min_price = infoDict.get(u'最低')
        # print("Max: %s" % max_price)
        # print("Min: %s\n" % min_price)

        x.add_row([stockName_pinyin, current_price, change_price, change_rate, max_price, min_price])

    print('%s' % x)

    time.sleep(30)