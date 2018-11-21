#!/usr/bin/env python
# -*- coding: utf-8 -*-

#---------------------------------------
#   Program: stock_v0.2.py
#   Version: 0.2
#   Author: Alan Tang
#   Date: 2017-08-22
#   Language: Python 2.7.12
#   Description: Get stock data from a list
#---------------------------------------

from __future__ import print_function
import urllib2
from bs4 import BeautifulSoup

stock_list = ['002689', '601628', '600326']

baseUrl = "https://gupiao.baidu.com/stock/"

for stock in stock_list:
    if stock.startswith('00'):
        code = 'sz'
    elif stock.startswith('60'):
        code = 'sh'

    full_url = baseUrl + code + stock + '.html'
    # print(full_url)

    page = urllib2.urlopen(full_url)
    html = page.read()
    # print(html)

    soup = BeautifulSoup(html, 'html.parser')

    stockInfo = soup.find('div', attrs={'class':'stock-bets'})
    stockName = stockInfo.find_all(attrs={'class':'bets-name'})[0].text.split()[0]
    print("Stock Name: %s" % stockName)

    price_class = soup.find('div', attrs={'class':'price'})
    # print(price_class)
    print("Current Price: %s" % price_class.strong.string)

    price_range = price_class.find_all('span')
    # for i in price_range:
    #     print(i.string)
    print("Change: %s" % price_range[0].string)
    print("Rate: %s" % price_range[1].string)

    infoDict = {}
    keyList = stockInfo.find_all('dt')
    valueList = stockInfo.find_all('dd')

    for i in range(len(keyList)):
        key = keyList[i].text
        val = valueList[i].text
        infoDict[key] = val

    # print(infoDict)
    print("Max: %s" % infoDict.get(u'最高'))
    print("Min: %s\n" % infoDict.get(u'最低'))
