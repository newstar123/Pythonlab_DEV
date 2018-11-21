#!/usr/bin/env python
#coding:utf-8
#可变长度的参数

# 非关键字可变长参数（元组）
def tupleVarArgs(arg1, arg2='defaultB', *theRest):
    'display regular args and non-keyword variable args'
    print 'formal arg1:', arg1
    print 'formal arg2:', arg2
    for eachXtrArg in theRest:
        print 'another arg:', eachXtrArg

print "==tupleVarArgs('abc')==:"
tupleVarArgs('abc')

print ''

print "==tupleVarArgs(23, 4.56)==:"
tupleVarArgs(23, 4.56)

print ''

print "==tupleVarArgs('abc', 123, 'xyz', 456.789)==:"
tupleVarArgs('abc', 123, 'xyz', 456.789)
print ''

print '*'*60

def dictVarArgs(arg1, arg2='defaultB', **theRest):
    'display 2 regular args and keyword variable args'
    print 'formal arg1:', arg1
    print 'formal arg2:', arg2
    for eachXtrArg in theRest:
        print 'Xtra arg %s: %s' % \
            (eachXtrArg, str(theRest[eachXtrArg]))

print "++dictVarArgs(1220, 740.0, c='grail')++:"
dictVarArgs(1220, 740.0, c='grail')
print ''

print "++dictVarArgs(arg2='tales', c=123, d='poe', arg1='mystery')++:"
dictVarArgs(arg2='tales', c=123, d='poe', arg1='mystery')
print ''

print "++dictVarArgs('one', d=10, e='zoo', men=('freud', 'gaudi'))++:"
dictVarArgs('one', d=10, e='zoo', men=('freud', 'gaudi'))
print ''

print '*'*60

def newfoo(arg1, arg2, *nkw, **kw):
    'display regular args and all variable args'
    print 'arg1 is:', arg1
    print 'arg2 is:', arg2
    for eachNKW in nkw:
        print 'additional non-keyword arg:', eachNKW
    for eachKW in kw:
        print "additional keyword arg '%s': %s" % \
            (eachKW, kw[eachKW])

print "==newfoo('wolf', 3, 'projects', freud=90, gamble=96)==:"
newfoo('wolf', 3, 'projects', freud=90, gamble=96)
print ''

print '*'*60

print "==newfoo(2,4,*(6,8),**{'foo':10, 'bar':12})==:"
newfoo(2,4,*(6,8),**{'foo':10, 'bar':12})
print ''

print '*'*60

aTuple = (6, 7, 8)
aDict = {'z': 9}
newfoo(1, 2, 3, x=4, y=5, *aTuple, **aDict)