#!/usr/bin/env python
#coding:utf-8
#该脚本产生一个较大的随机数集合，然后过滤出所有的偶数，留给我们一个需要的数据集

'''
from random import randint

def odd(n):
    return n%2

allNums = []
for eachNum in range(9):
    allNums.append(randint(1, 99))
print filter(odd, allNums)
'''

#第一次重构：用一个lambda表达式替换odd()函数
'''
from random import randint

allNums = []
for eachNum in range(9):
    allNums.append(randint(1, 99))
print filter(lambda n: n%2, allNums)
'''

#第二次重构：列表解析，list综合使用替代filter()
'''
from random import randint

allNums = []
for eachNum in range(9):
    allNums.append(randint(1, 99))
print [n for n in allNums if n%2]
'''

#第三次重构：去除暂时变量
from random import randint

print [n for n in [randint(1, 99) for i in range(9)] if n%2]




