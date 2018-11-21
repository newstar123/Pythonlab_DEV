#!/usr/bin/env python
# -*- coding: utf-8 -*-

#---------------------------------------
#   Program: stock_v0.9.py
#   Version: 0.9
#   Author: Alan Tang
#   Date: 2017-09-01
#   Language: Python 3.6.2
#   Description: 使用Python3
#---------------------------------------

import requests
from bs4 import BeautifulSoup
from prettytable import PrettyTable
from xpinyin import Pinyin
import time

p = Pinyin()

stock_dict = {
    '上证指数': '000001',
    # '西藏天路': '600326',
    '中国人寿': '601628',
    '远大智能': '002689',
    # '尚荣医疗': '002551',
    # '唐山港': '601000',
    # '常铝股份': '002160',
    # '珠海港': '000507',
    # '兴业矿业': '000426',
    # '西部建设': '002302'
}

baseUrl = "https://gupiao.baidu.com/stock/"

while True:
    x = PrettyTable(["Stock Name", "Current Price", "Rate", "Change", "Max", "Min", "Time"])
    x.align["Stock Name"] = "l"
    x.padding_width = 1

    for key, value in stock_dict.items():
        if value.startswith('00') and value != '000001':
            stockCode = 'sz'
        elif value.startswith('60') or value == '000001':
            stockCode = 'sh'

        full_url = baseUrl + stockCode + value + '.html'

        page = requests.get(full_url)
        page.encoding = page.apparent_encoding
        html = page.text

        soup = BeautifulSoup(html, 'html.parser')

        stockInfo = soup.find('div', attrs={'class':'stock-bets'})
        stockName = stockInfo.find_all(attrs={'class':'bets-name'})[0].text.split()[0]
        stockTime = stockInfo.find_all(attrs={'class': 'state'})[0].text.split()[2]

        # 汉字转换成拼音
        stockName_pinyin = p.get_initials(stockName, u'')

        price_class = soup.find('div', attrs={'class':'price'})
        current_price = price_class.strong.string

        price_range = price_class.find_all('span')
        change_price = price_range[0].string
        change_rate = price_range[1].string

        infoDict = {}
        keyList = stockInfo.find_all('dt')
        valueList = stockInfo.find_all('dd')

        for i in range(len(keyList)):
            key = keyList[i].text
            val = valueList[i].text
            infoDict[key] = val

        max_price = infoDict.get(u'最高')
        min_price = infoDict.get(u'最低')

        x.add_row([stockName, str(current_price), str(change_rate), str(change_price), str(max_price), str(min_price), stockTime])

    print('%s' % x)

    time.sleep(30)