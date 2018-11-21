# -*- coding: utf-8 -*-

#---------------------------------------
#   Program: stock_alert_v0.3.py
#   Version: 0.3
#   Author: Alan Tang
#   Date: 2017-09-08
#   Language: Python 3.6.2
#   Description: 指定运行时间段
#---------------------------------------

import requests
from bs4 import BeautifulSoup
from prettytable import PrettyTable
from xpinyin import Pinyin
import time
from sendEmail import SendEmail

p = Pinyin()

mailto_list = ['15995869332@139.com', 'mchina_tang@qq.com']
mail_host = "smtp.126.com"          #定义smtp主机
mail_user = "mchina_tang@126.com"   #用户名
mail_pass = "xxxx"       #口令
# mail = SendEmail(mail_host, mail_user, mail_pass)

stock_dict = {
    '上证指数': '000001',
    # '西藏天路': '600326',
    '中国人寿': '601628',
    # '远大智能': '002689',
    # '尚荣医疗': '002551',
    # '唐山港': '601000',
    # '常铝股份': '002160',
    # '珠海港': '000507',
    # '兴业矿业': '000426',
    # '西部建设': '002302'
}

stock_alert_value_high = {
    '中国人寿': 28.00,
    '远大智能': 6.85,
}

stock_alert_value_low = {
    '中国人寿': 27.50,
    '远大智能': 6.60,
}

baseUrl = "https://gupiao.baidu.com/stock/"

def getCurrentTime():
    return time.strftime('%H:%M:%S', time.localtime(time.time()))

while True:
    mail = SendEmail(mail_host, mail_user, mail_pass)
    x = PrettyTable(["Stock Name", "Current Price", "Rate", "Change", "Max", "Min", "Time"])
    x.align["Stock Name"] = "l"
    x.padding_width = 1

    currentTime = getCurrentTime()

    if currentTime >= "09:30:00" and currentTime <= "11:30:00" or currentTime >= "13:00:00" and currentTime <= "15:03:00":
        for key, value in stock_dict.items():
            if value.startswith('00') and value != '000001':
                stockCode = 'sz'
            elif value.startswith('60') or value == '000001':
                stockCode = 'sh'

            full_url = baseUrl + stockCode + value + '.html'


            try:
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
                # 当前价格
                current_price = price_class.strong.string

                # 达到设定高值发送邮件
                for k, v in stock_alert_value_high.items():
                    if k == stockName:
                        if float(current_price) >= v:
                            if mail.sendTxtMail(mailto_list, k+"卖出提醒-" + current_price, k+"上涨到" + current_price + "了。"):
                                pass
                                # print(k+" 提醒邮件发送成功！")
                            else:
                                pass
                                # print(k+" 提醒邮件发送失败！")
                        else:
                            pass
                            # print(k+" 未达预设值")
                # 达到设定低值
                for k, v in stock_alert_value_low.items():
                    if k == stockName:
                        if float(current_price) <= v:
                            if mail.sendTxtMail(mailto_list, k + "买入提醒-" + current_price, k + "下降到" + current_price + "了。"):
                                pass
                                # print(k+" 提醒邮件发送成功！")
                            else:
                                pass
                                # print(k+" 提醒邮件发送失败！")
                        else:
                            pass
                            # print(k+" 未达预设值")

                price_range = price_class.find_all('span')
                # 价格变化值
                change_price = price_range[0].string
                # 价格变化幅度
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
            except Exception as e:
                print("Error: %s" % (e))

        print('%s' % x)

        time.sleep(30)
    else:
        print("%s Not in the trading time." % currentTime)
        time.sleep(60)