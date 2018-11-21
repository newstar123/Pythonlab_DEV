#!/usr/bin/env python
#coding:utf-8
'''
编写登陆接口
- 输入用户名密码
- 认证成功后显示欢迎信息
- 输错三次后锁定
'''

account_file = "account.txt"
lock_file = "lock.txt"

for i in range(3):	# for #1
	username = raw_input("Please input username: ").strip()
	password = raw_input("Please input password: ").strip()
	
	if len(username) != 0 and len(password) != 0:
		loginSuccess = False
		f = file(account_file)
		for line in f.readlines():	# for #2
			line = line.split()
			if username == line[0] and password == line[1]:
				# username and password are correct
				print "Welcome %s login system!" % username
				loginSuccess = True
				break	# 跳出for #2循环，至第27行
		# print loginSuccess
		if loginSuccess is True:
			break	# 跳出for #1循环，至第32行
	else:
		continue

else:
	f = file(lock_file, 'a')
	f.write('%s\n' % username)
	f.close()



