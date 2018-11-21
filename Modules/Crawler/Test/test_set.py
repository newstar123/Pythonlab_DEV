# -*- coding: utf-8 -*-

#---------------------------------------
#   程序：test_set.py
#   版本：0.1
#   作者：ctang
#   日期：2016-01-29
#   语言：Python 2.7.10
#   说明：集合
#   Python提供了set这种数据结构. set是一种无序的, 不包含重复元素的结构. 一般用来测试是否已经包含了某元素, 或者用来对众多元素们去重.
#   与数学中的集合论同样, 他支持的运算有交, 并, 差, 对称差.
#---------------------------------------

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print basket

print 'orange' in basket
print 'crabgrass' in basket

a = set('abracadabra')
b = set('alacazam')

print a
print a - b     # 集合a中包含元素
print a | b     # 集合a或b中包含的所有元素
print a & b     # 集合a和b中都包含了的元素
print a ^ b     # 不同时包含于a和b的元素