#!/usr/bin/env python
# -*- coding: utf-8 -*-

#---------------------------------------
#   Program: stock_v0.1.py
#   Version: 0.1
#   Author: Alan Tang
#   Date: 2017-08-22
#   Language: Python 2.7.12
#   Description: Get single stock data
#---------------------------------------

from __future__ import print_function
import urllib2
from bs4 import BeautifulSoup

url = "https://gupiao.baidu.com/stock/sh601628.html"

page = urllib2.urlopen(url)
html = page.read()
# print(html)

soup = BeautifulSoup(html, 'html.parser')
price_class = soup.find('div', attrs={'class':'price'})
# print(price_class)
print("Current Price: %s" % price_class.strong.string)

price_range = price_class.find_all('span')
# for i in price_range:
#     print(i.string)
print("Change: %s" % price_range[0].string)
print("Rate: %s" % price_range[1].string)