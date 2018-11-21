# -*- coding: utf-8 -*-

#---------------------------------------
#   Program: acquiring_all_stock_data_v0.4.py
#   Version: 0.4
#   Author: Alan Tang
#   Date: 2017-08-31
#   Language: Python 3.6.2
#   Description: 加入日期和今日收盘价
#---------------------------------------

import requests
from bs4 import BeautifulSoup
import re
from pymongo import MongoClient

conn = MongoClient('mongodb://admin:admin@localhost:27017/')
db = conn['stock']

def getHTMLText(url):
    try:
        r = requests.get(url)
        # 如果响应的状态码不为200，Response.raise_for_status()会抛出HTTPError 异常
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def getStockList(lst, stockURL):
    html = getHTMLText(stockURL)
    soup = BeautifulSoup(html, 'html.parser')
    a = soup.find_all('a')
    for i in a:
        try:
            href = i.attrs['href']
            lst.append(re.findall(r"[s][hz][63]0[0123]\d{3}", href)[0])
        except:
            continue

def getStockInfo(lst, stockURL):
    count = 0
    for stock in lst:
        url = stockURL + stock + ".html"
        # print(url)
        html = getHTMLText(url)
        try:
            if html == "":
                continue
            infoDict = {}
            soup = BeautifulSoup(html, 'html.parser')
            stockInfo = soup.find('div', attrs={'class':'stock-bets'})

            stockName = stockInfo.find_all(attrs={'class':'bets-name'})[0]
            stockCode = re.findall(r"\d{6}", stockName.text.split()[1])[0]
            stockDate = stockInfo.find_all(attrs={'class': 'state'})[0].text.split()[1]

            # 当前价格
            price_class = soup.find('div', attrs={'class': 'price'})
            current_price = price_class.strong.string

            infoDict.update({'股票名称': stockName.text.split()[0]})
            infoDict.update({'股票代码': stockCode})
            infoDict.update({'数据日期': stockDate})
            infoDict.update({'今收': current_price})

            keyList = stockInfo.find_all('dt')
            valueList = stockInfo.find_all('dd')
            for i in range(len(keyList)):
                key = keyList[i].text
                val = valueList[i].text.strip('\n').strip()
                infoDict[key] = val

            db.all_stock_data.insert(infoDict)
            count = count + 1
            print("\rCurrent progress: %.2f%%" % (count*100/len(lst)))
        except Exception as e:
            count = count + 1
            print("\rCurrent progress: %.2f%%" % (count*100/len(lst)))
            print("Error: %s - %s" % (stock, e))
            continue

def main():
    stock_list_url = 'http://quote.eastmoney.com/stocklist.html'
    stock_info_url = 'https://gupiao.baidu.com/stock/'
    stock_list = []
    getStockList(stock_list, stock_list_url)
    getStockInfo(stock_list, stock_info_url)

if __name__ == '__main__':
    main()