# -*- coding:utf-8 -*-
# 验证代理
import urllib
import socket

# 设置全局超时时间为3s，也就是说，如果一个请求3s内还没有响应，就结束访问，并返回timeout（超时）
socket.setdefaulttimeout(3)

f = open("proxy.txt")
lines = f.readlines()
proxys = []

for i in range(0, len(lines)):
	ip = lines[i].strip("\n").split("\t")
	proxy_host = "http://" + ip[0] + ":" + ip[1]
	proxy_temp = {"http":proxy_host}
	proxys.append(proxy_temp)

url = "http://ip.chinaz.com/getip.aspx"

for proxy in proxys:
	try:
		res = urllib.urlopen(url, proxies=proxy).read()
		print res + " 完整地址：" + str(proxy['http'])
	except Exception, e:
		#print proxy
		#print e
		continue


