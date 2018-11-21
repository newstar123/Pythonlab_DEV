#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
面向对象编程
'''

'''
方法：
方法定义在类定义中，但只能被实例所调用，即：
1. 定义类（和方法）
2. 创建一个实例
3. 用这个实例调用方法
'''
class MyDataWithMethod(object):
    def printFoo(self):
        print 'You invoked printFoo()!'

'''
myObj = MyDataWithMethod()
myObj.printFoo()

'''

#创建一个类（类定义）
class AddrBookEntry(object):
    'address book entry class'
    def __init__(self, nm, ph):
        self.name = nm
        self.phone = ph
        print 'Created instance for:', self.name
    def updatePhone(self, newph):
        self.phone = newph
        print 'Updated phone# for:', self.name

'''
#创建实例（实例化）
john = AddrBookEntry('John Doe', '408-555-1212')
jane = AddrBookEntry('Jane Doe', '650-555-1212')

print john
print john.name
print john.phone
print jane.name
print jane.phone

john.updatePhone('415-555-1212')
print john.phone

'''

#创建子类
class EmplAddrBookEntry(AddrBookEntry):
    'Employee Address Book Entry class'
    def __init__(self, nm, ph, id, em):
        AddrBookEntry.__init__(self, nm, ph)
        self.empid = id
        self.email = em

    def updateEmail(self, newem):
        self.email = newem
        print 'Updated e-mail address for:', self.name

'''
john = EmplAddrBookEntry('John Doe', '408-555-1212', 42, 'john@spam.doe')

print john
print john.name
print john.phone
print john.email
john.updatePhone('415-555-1212')
print john.phone
john.updateEmail('john@doe.spam')
print john.email

'''

#决定类的属性
class MyClass(object):
    'MyClass class definition'
    myVersion = '1.1'
    def showMyVersion(self):
        print MyClass.myVersion

'''
print dir(MyClass)
print MyClass.__dict__

print ''

#特殊的类属性
print '## Special Class Attributes ##'
print MyClass.__name__
print MyClass.__doc__
print MyClass.__bases__
print MyClass.__module__
print MyClass.__class__

'''

#子类和派生
class Parent(object):   #定义父类
    def parentMethod(self):
        print 'calling parent method'

class Child(Parent):    #定义子类
    def childMethod(self):
        print 'calling child method'

'''
p = Parent()        #父类的实例
p.parentMethod()
c = Child()         #子类的实例
c.childMethod()     #子类调用它的方法
c.parentMethod()    #调用父类的方法

'''

#继承
class P(object):
    'P class'
    def __init__(self):
        print 'created an instance of', \
            self.__class__.__name__

class C(P):
    pass

'''
p = P()
print p.__class__   #实例对应的类
print P.__bases__   #类的所有父类构成的元组
print p.__doc__     #类的文档字符串

c = C()
print c.__class__
print C.__bases__
print C.__doc__

'''

#通过继承覆盖方法
class P2(object):
    def foo(self):
        print 'Hi, I am P-foo()'

p2 = P2()
p2.foo()

class C2(P2):
    def foo(self):
        print 'Hi, I am C2-foo()'

c2 = C2()
c2.foo()

#调用基类方法
P2.foo(c2)

#显式调用基类方法
class C3(P2):
    def foo(self):
        P2.foo(self)
        print 'Hi, I am C3-foo()'

c3 = C3()
c3.foo()

#使用super()内建方法
class C4(P2):
    def foo(self):
        super(C4, self).foo()
        print 'Hi, I am C4-foo()'

c4 = C4()
c4.foo()









