#!/usr/bin/env python
#coding:utf-8
'''
把列表用作队列来存储和取回菜单驱动应用里面输入的字符串
队列：先进先出（FIFO）的数据结构
'''

# 初始化堆栈
queue = []

def enQ():
    queue.append(raw_input("Enter new string: ").strip())

def deQ():
    if len(queue) == 0:
        print "Cannot dequeue from an empty queue!"
    else:
        print 'Removed [', `queue.pop(0)`, ']'

def viewQ():
    print queue

CMDs = {'e': enQ, 'd': deQ, 'v': viewQ}

def showmenu():
    pr = """
(E)nqueue
(D)equeue
(V)iew
(Q)uit

Enter choice: """

    while True:
        while True:
            try:
                choice = raw_input(pr).strip()[0].lower()
            except (EOFError,KeyboardInterrupt,IndexError):
                choice = 'q'

            print '\nYou picked: [%s]' % choice

            if choice not in 'edvq':
                print 'Invalid option, try again'
            else:
                break

        if choice == 'q':
            break
        CMDs[choice]()

if __name__ == '__main__':
    showmenu()



