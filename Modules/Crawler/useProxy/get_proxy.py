# -*- coding:utf-8 -*-
# 获取代理
import urllib2
from bs4 import BeautifulSoup

User_Agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0'
header = {}
header['User-Agent'] = User_Agent

url = 'http://www.xicidaili.com/nn/1'
req = urllib2.Request(url, headers = header)
res = urllib2.urlopen(req).read()

soup = BeautifulSoup(res, "html.parser")
ips = soup.findAll('tr')
f = open("proxy.txt","w")

#print ips

for x in range(1, len(ips)):
	ip = ips[x]
	tds = ip.findAll('td')
	ip_temp = tds[2].contents[0] + "\t" + tds[3].contents[0] + "\n"
	f.write(ip_temp)

