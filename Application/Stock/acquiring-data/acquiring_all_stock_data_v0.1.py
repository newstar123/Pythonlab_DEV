# -*- coding: utf-8 -*-

#---------------------------------------
#   Program: acquiring_all_stock_data_v0.1.py
#   Version: 0.1
#   Author: Alan Tang
#   Date: 2017-08-29
#   Language: Python 3.6.2
#   Description: 获取沪市A股，深市A股，创业板，中小板所有股票数据
#---------------------------------------

# from __future__ import print_function
# from __future__ import division
# import uniout
import requests
from bs4 import BeautifulSoup
import re

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
            # lst.append(re.findall(r"([s][hz](600|601|603|000|002|300)\d{3})", href)[0][0])
            lst.append(re.findall(r"[s][hz][63]0[0123]\d{3}", href)[0])
        except:
            continue

def getStockInfo(lst, stockURL, filePath):
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

            name = stockInfo.find_all(attrs={'class':'bets-name'})[0]
            infoDict.update({'股票名称': name.text.split()[0]})

            keyList = stockInfo.find_all('dt')
            valueList = stockInfo.find_all('dd')
            for i in range(len(keyList)):
                key = keyList[i].text
                val = valueList[i].text
                infoDict[key] = val

            with open(filePath, 'a') as f:
                f.write(str(infoDict) + '\n')
                # print(infoDict)
                count = count + 1
                print("\r当前进度：%.2f%%" % (count*100/len(lst)))
        except Exception as e:
            count = count + 1
            print("\r当前进度：%.2f%%" % (count*100/len(lst)))
            print(e)
            continue

def main():
    stock_list_url = 'http://quote.eastmoney.com/stocklist.html'
    stock_info_url = 'https://gupiao.baidu.com/stock/'
    output_file = 'F:/stockInfo.txt'
    stock_list = []
    getStockList(stock_list, stock_list_url)
    # print(stock_list)
    getStockInfo(stock_list, stock_info_url, output_file)

if __name__ == '__main__':
    main()