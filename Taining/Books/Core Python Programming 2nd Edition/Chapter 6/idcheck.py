#!/usr/bin/env python
#coding:utf-8

import string

alphas = string.letters + '_'
nums = string.digits

print 'Welcome to the Identifier Checker v1.0'
print 'Testees must be at least 2 chars long.'

myInput = raw_input('Identifier to test? ')

if len(myInput) > 1:
    if myInput[0] not in alphas:
        print '''invalid: first symbol must be alphabetic'''
    else:
        for otherChar in myInput[1:]:
            if otherChar not in alphas + nums:
                print '''invalid: remaning symbols must be alphanumric'''
                break
        else:
            print "okay as an identifier"



'''
运行结果：
Welcome to the Identifier Checker v1.0
Testees must be at least 2 chars long.
Identifier to test? abc
okay as an identifier

Welcome to the Identifier Checker v1.0
Testees must be at least 2 chars long.
Identifier to test? 123abc
invalid: first symbol must be alphabetic

Welcome to the Identifier Checker v1.0
Testees must be at least 2 chars long.
Identifier to test? abc%^
invalid: remaning symbols must be alphanumric
'''
