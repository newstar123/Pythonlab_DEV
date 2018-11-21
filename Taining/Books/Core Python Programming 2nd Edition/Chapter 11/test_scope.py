#!/usr/bin/env python
#coding:utf-8

#如果将全局变量的名字声明在一个函数体内的时候，全局变量的名字能被局部变量给覆盖掉。
def foo():
    print "\ncalling foo()..."
    bar = 200
    print "in foo(), bar is", bar

bar = 100
print "in __main__, bar is", bar
foo()
print "\nin __main__, bar is (still)", bar

print ''
print '+'*40
print ''

#global语句，明确地引用一个已命名的全局变量
is_this_global = 'xyz'

def foo2():
    global is_this_global
    this_is_local = 'abc'
    is_this_global = 'def'
    print this_is_local + is_this_global

foo2()

print is_this_global

