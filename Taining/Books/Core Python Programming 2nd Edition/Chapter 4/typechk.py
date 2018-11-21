#!/usr/bin/env python
#coding:utf-8

def displayNumType(num):
    print num, 'is',
    if isinstance(num, (int, long, float, complex)):
        print 'a number of type:', type(num).__name__
    else:
        print 'not a number at all!!'

displayNumType(-69)
displayNumType(99999999999999999999999999999999)
displayNumType(98.6)
displayNumType(-5.2+1.9j)
displayNumType('xxx')



"""
运行结果：
-69 is a number of type: int
99999999999999999999999999999999 is a number of type: long
98.6 is a number of type: float
(-5.2+1.9j) is a number of type: complex
xxx is not a number at all!!
"""