#!/usr/bin/env python
# -*- coding: utf-8 -*-

#---------------------------------------
#   程序：test_login_rt.py
#   版本：0.1
#   版本：0.2, 修正检查Ticket更新的逻辑
#   版本：0.3, 将最新一条更新信息附加到邮件正文中
#   版本：0.4, 如果最后修改人是自己，则不发送邮件
#   作者：ctang
#   日期：2016-02-24
#   语言：Python 2.7.10
#   说明：测试登录RT
#---------------------------------------

import os
import urllib
import urllib2
import cookielib
import re
import time
from bs4 import BeautifulSoup
from sendEmail import SendEmail

mailto_list = ['15995869332@139.com', 'tangchao@beyondsoft.com']
mail_host = "smtp.126.com"      #定义smtp主机
mail_user = "mchina_tang@126.com"       #用户名
mail_pass = "xxxx"   #口令
mail = SendEmail(mail_host, mail_user, mail_pass)

#获取当前时间
def getCurrentTime():
    return time.strftime('[%Y-%m-%d %H:%M:%S]', time.localtime(time.time()))

#获取登录RT时隐藏附加的一个Next值
def getNext(data):
    soup = BeautifulSoup(data, "html.parser")
    next = soup.find("input", {"name": "next"})['value']
    return next

#通过详情页获取最后更新时间和人
def getLatestUpdated(url):
    #print url
    op = opener.open(url)
    data = op.read()
    #return data
    soup = BeautifulSoup(data, "html.parser")
    latestUpdated = soup.find("tr", {"class": "date updated"})
    result = latestUpdated.a.string
    return result

#通过详情页获取最新一条更新信息
def getLatestUpdatedMessage(url):
    op = opener.open(url)
    data = op.read()
    soup = BeautifulSoup(data, "html.parser")
    #latestMessage = soup.find_all("div", {"class": "message-stanza"})
    latestMessage = soup.find_all("div", {"class": "messagebody"})
    result = latestMessage[-1]
    return result

def getOpener(head):
    cookie = cookielib.CookieJar()
    handler = urllib2.HTTPCookieProcessor(cookie)
    opener = urllib2.build_opener(handler)
    header = []
    for key, value in head.items():
        elem = (key, value)
        header.append(elem)
    opener.addheaders = header
    return opener

header = {
    'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Host': 'tickets.theportalgrp.com',
}

url = 'http://tickets.theportalgrp.com/rt/'
detail_url = 'http://tickets.theportalgrp.com/rt/Ticket/Display.html?id='
opener = getOpener(header)
op = opener.open(url)
data = op.read()
next = getNext(data.decode())

url += 'NoAuth/Login.html'
username = 'chao.tang'
password = 'xxxx'
postDict = {
    'user': username,
    'pass': password,
    'next': next
}

postData = urllib.urlencode(postDict)
op = opener.open(url, postData)
data = op.read()

# My Tickets
print "My Tickets"
pattern_myTicket = re.compile('<td.*?align="right"><a.*?>(.*?)</a></td>.*?<td.*?><a.*?>(.*?)</a></td>.*?<td.*?>(.*?)</td>.*?<td.*?>(.*?)</td>.*?<td.*?>(.*?)</td>.*?<td.*?align="right"><a.*?>Take</a></td>.*?</tr>', re.S)
myTicket = re.findall(pattern_myTicket, str(data))
# 如果没有maxTicket.txt文件，则新建空文件，以便下面程序读取
if not os.path.exists('maxTicket.txt'):
    open('maxTicket.txt', 'w')
# 如果文件夹updated不存在，则新建文件夹
parent_path = os.getcwd()
path = parent_path+'/updated/'
if not os.path.exists(path):
    os.mkdir(path)
for item in myTicket:
    #print item
    # 处理新Ticket，读取文本文件里的max, 遍历ticket，然后和max比较，如果ticket>max，修改max，发送邮件
    m_handler = open('maxTicket.txt', 'r')
    max = m_handler.readline()
    if item[0] > max:
        m_handler = open('maxTicket.txt', 'w')
        m_handler.write(item[0])
        m_handler.close()
        if mail.sendTxtMail(mailto_list, "新任务New Ticket "+item[0]+" Come In", "Hello CTANG,<br /><p>有一个新的Ticket "+item[0]+", 请及时处理！</p><p>http://tickets.theportalgrp.com/rt/Ticket/Display.html?id="+item[0]+"</p>"):
            print getCurrentTime() + " New Ticket "+item[0]+" 提醒邮件发送成功！"
        else:
            print getCurrentTime() + " New Ticket "+item[0]+" 提醒邮件发送失败！"
    else:
        print getCurrentTime() + " 没有新的Ticket信息!"
    # 处理最新更新
    realLatestUpdated = getLatestUpdated(detail_url+item[0])
    updatedBy = realLatestUpdated.split('by')[1].strip()
    #print updatedBy
    if os.path.exists(path+item[0]):
        l_handler = open(path+item[0], 'r')
        savedLastUpdated = l_handler.readline()
        if savedLastUpdated != '':
            if realLatestUpdated != savedLastUpdated:
                # 获取最新一条更新信息
                latestMessage = str(getLatestUpdatedMessage(detail_url+item[0]))
                #print latestMessage
                # 将最新更新的时间和人写入Ticket Number对应的文本文件
                l_handler = open(path+item[0], 'w')
                l_handler.write(realLatestUpdated)
                l_handler.close()
                if updatedBy != 'Chao Tang':
                    # 发送邮件
                    if mail.sendTxtMail(mailto_list, "更新信息Ticket "+item[0]+" Has Update", "Hi CTANG,<br /><p>Ticket "+item[0]+" 有一个新的更新信息, 请及时处理！</p><p>最新一条更新信息：</p><p>"+latestMessage+"</p><p>http://tickets.theportalgrp.com/rt/Ticket/Display.html?id="+item[0]+"</p>"):
                        print getCurrentTime() + " Updated Ticket "+item[0]+" 邮件发送成功！"
                    else:
                        print getCurrentTime() + " Updated Ticket "+item[0]+" 邮件发送失败！"
                else:
                    print getCurrentTime() + " "+item[0]+" 最新更新By Chao Tang."
            else:
                print getCurrentTime() + " Ticket "+item[0]+" 没有新的Update信息！"
        else:
            l_handler = open(path+item[0], 'w')
            l_handler.write(realLatestUpdated)
            l_handler.close()
            print getCurrentTime() + " 记录新分配Ticket "+item[0]+" 时未获得的Update信息！"
    else:
        if realLatestUpdated != '':
            l_handler = open(path+item[0], 'w')
            l_handler.write(realLatestUpdated)
            l_handler.close()
            print getCurrentTime() + " 记录新的 "+item[0]+" Update信息！"
        else:
            open(path+item[0], 'w')
            print getCurrentTime() + " "+item[0]+" Update信息为空，将在稍微记录！"

# kangjun.xu & sam.cui Tickets
'''
print "kangjun.xu & sam.cui Tickets"
pattern_items = re.compile('<td.*?align="right">.*?<b><a.*?>(.*?)</a></b></td>.*?<td.*?><b><a.*?>(.*?)</a></b></td>.*?<td.*?>(.*?)</td>.*?<td.*?>(.*?)</td>.*?<td.*?>(.*?)</td>.*?<td.*?>(.*?)</td>.*?</tr>.*?<td.*?><small>(.*?)</small></td>.*?<td.*?><small>(.*?)</small></td>.*?<td.*?><small>(.*?)</small></td>.*?<td.*?><small>(.*?)</small></td>.*?<td.*?><small>(.*?)</small></td>', re.S)
items = re.findall(pattern_items, str(data))
for item in items:
    #if item[4] == 'sam.cui':
    print item
'''

