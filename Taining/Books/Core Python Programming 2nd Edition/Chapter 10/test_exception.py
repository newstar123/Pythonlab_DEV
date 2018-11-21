#!/usr/bin/env python
#coding:utf-8

#一个except
def safe_float1(obj):
    try:
        retval = float(obj)
    except ValueError:
        retval = 'could not convert non-number to float'
    return retval

#多个except
def safe_float2(obj):
    try:
        retval = float(obj)
    except ValueError:
        retval = 'could not convert non-number to float'
    except TypeError:
        retval = 'object type cannot be converted to float'
    return retval

#处理多个异常的except语句
def safe_float3(obj):
    try:
        retval = float(obj)
    except (ValueError, TypeError):
        retval = 'argument must be a number or numeric string'
    return retval

#异常参数
def safe_float4(obj):
    try:
        retval = float(obj)
    except (ValueError, TypeError), diag:
        retval = str(diag)
    return retval


#print safe_float1('12.34')  #12.34
#print safe_float1('bad input')  #could not convert non-number to float

#print safe_float2('xyz')    #could not convert non-number to float
#print safe_float2(())   #object type cannot be converted to float

#print safe_float3('Spanish Inquisition')    #argument must be a number or numeric string
#print safe_float3([])   #argument must be a number or numeric string

#print safe_float4('xyz')    #could not convert string to float: xyz
print safe_float4({})   #float() argument must be a string or a number



