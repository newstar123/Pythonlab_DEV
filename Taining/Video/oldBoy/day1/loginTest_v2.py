#!/usr/bin/env python
#coding:utf-8
'''
编写登陆接口 - v2
- 输入用户名密码
- 认证成功后显示欢迎信息
- 输错三次后锁定

1. 输入username
2. 判断是否被锁定
	a. 若被锁定，打印一句话后直接退出；
	b. 若未被锁定，继续执行下面的代码；
3. 判断该username是否在account_list中
	a. 如果在，则提示输入password，输错三次，锁定该帐户，再继续提示输入username；
	b. 如果不在, 循环提示输入username；
'''

account_file = "account.txt"
lock_file = "lock.txt"

# 读取用户名/密码信息至一个列表
f = file(account_file)
account_list = f.readlines()
f.close()

# print account_list

while True: # while #1
	# 读取lock_file至列表
	f = open(lock_file)
	lock_list = []
	for i in f.readlines():	# for #1
		i = i.strip('\n')
		lock_list.append(i)
	f.close()

	# print lock_list

	loginSuccess = False
	username = raw_input("Please enter username: ").strip()

	if username in lock_list:
		print "%s账户被锁定，无法登陆！" % username
		break

	for line in account_list:	# for #2
		line = line.split()
		if username == line[0]:	# 输入了正确的用户名
			for i in range(3):	# for #3
				password = raw_input("Please enter password: ").strip()
				if password == line[1]:
					print "Welcome %s login system!" % username
					loginSuccess = True
					break	# 跳出for #3循环，至第55行

			else:
				print "输入3次密码错误，锁定%s!" % username
				f = open(lock_file, 'a')
				f.write('%s\n' % username)
				f.close()

			if loginSuccess == True:
				break	# 跳出for #2循环，至第64行

	if loginSuccess == True:
		break	# 跳出while #1循环

