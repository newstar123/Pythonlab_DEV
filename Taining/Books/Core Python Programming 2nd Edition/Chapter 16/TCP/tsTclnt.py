#!/usr/bin/env python
#coding:utf-8
#创建一个TCP客户端，程序会提示用户输入要传给服务器的信息，显示服务器返回的加了时间戳的结果。

from socket import *

# HOST = 'localhost'
HOST = '10.10.73.3'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
	data = raw_input('> ')
	if not data:
		break
	tcpCliSock.send(data)
	data = tcpCliSock.recv(BUFSIZ)
	if not data:
		break
	print data

tcpCliSock.close()