#!/usr/bin/env python
#coding:utf-8

from time import ctime, sleep

def tsfunc(func):
    def wrappedFunc():
        print '[%s] %s() called' % (ctime(), func.__name__)
        return func()
    return wrappedFunc

@tsfunc
def foo():
    pass

foo()
sleep(4)

for i in range(2):
    sleep(1)
    foo()



'''
运行结果：
[Mon Nov 23 14:28:48 2015] foo() called
[Mon Nov 23 14:28:53 2015] foo() called
[Mon Nov 23 14:28:54 2015] foo() called
'''
