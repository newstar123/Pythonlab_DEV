#!/usr/bin/env python
#coding:utf-8
#有条件地执行代码

def foo():
    return True

def bar():
    'bar() does not do much'
    return True

foo.__doc__ = 'foo() does not do much'
foo.tester = '''
if foo():
    print 'PASSED'
else:
    print 'FAILED'
'''

#print dir()
#print type(foo)

for eachAttr in dir():
    obj = eval(eachAttr)
    if isinstance(obj, type(foo)):
        if hasattr(obj, '__doc__'):
            print '\nFunction "%s" has a doc string:\n\t%s' % (eachAttr, obj.__doc__)
        if hasattr(obj, 'tester'):
            print 'Function "%s" has a tester... executeing' % eachAttr
            exec obj.tester
        else:
            print 'Function "%s" has no tester... skipping' % eachAttr
    else:
        print '"%s" is not a function' % eachAttr


'''
运行结果：
"__builtins__" is not a function
"__doc__" is not a function
"__file__" is not a function
"__name__" is not a function
"__package__" is not a function

Function "bar" has a doc string:
	bar() does not do much
Function "bar" has no tester... skipping

Function "foo" has a doc string:
	foo() does not do much
Function "foo" has a tester... executeing
PASSED
'''

