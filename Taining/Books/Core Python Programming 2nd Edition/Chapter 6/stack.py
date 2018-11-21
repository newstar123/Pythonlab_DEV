#!/usr/bin/env python
#coding:utf-8
'''
把列表作为堆栈用于存储和取回输入的字符串
堆栈：后进先出（LIFO）的数据结构
'''

# 初始化堆栈
stack = []

def pushit():
    stack.append(raw_input("Enter new string: ").strip())

def popit():
    if len(stack) == 0:
        print "Cannot pop from an empty stack!"
    else:
        print 'Removed [', `stack.pop()`, ']'

def viewstack():
    print stack

CMDs = {'u': pushit, 'o': popit, 'v': viewstack}

def showmenu():
    pr = """
p(U)sh
p(O)p
(V)iew
(Q)uit

Enter choice: """

    while True:
        while True:
            try:
                choice = raw_input(pr).strip().lower()
            except (EOFError,KeyboardInterrupt,IndexError):
                choice = 'q'

            print '\nYou picked: [%s]' % choice

            if choice not in 'uovq':
                print 'Invalid option, try again'
            else:
                break

        if choice == 'q':
            break
        CMDs[choice]()

if __name__ == '__main__':
    showmenu()



