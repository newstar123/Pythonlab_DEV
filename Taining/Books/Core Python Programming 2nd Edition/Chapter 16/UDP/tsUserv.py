#!/usr/bin/env python
#coding:utf-8
#创建一个能接收客户端的消息，在消息前加一个时间戳后返回的UDP服务器。

from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpSerSock = socket(AF_INET, SOCK_DGRAM)
udpSerSock.bind(ADDR)

while True:
	print 'waiting for message...'
	data, addr = udpSerSock.recvfrom(BUFSIZ)
	udpSerSock.sendto('[%s] %s' % (ctime(), data), addr)
	print '...received from and returned to:', addr

udpSerSock.close()