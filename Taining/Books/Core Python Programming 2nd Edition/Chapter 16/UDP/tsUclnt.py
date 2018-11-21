#!/usr/bin/env python
#coding:utf-8
#创建一个UDP客户端，程序会提示用户输入要传给服务器的信息，显示服务器返回的加了时间戳的结果。

from socket import *

HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpCliSock = socket(AF_INET, SOCK_DGRAM)

while True:
	data = raw_input('> ')
	if not data:
		break
	udpCliSock.sendto(data, ADDR)
	data, ADDR = udpCliSock.recvfrom(BUFSIZ)
	if not data:
		break
	print data

udpCliSock.close()