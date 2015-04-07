
#!/usr/bin/env python  
# -*- coding: utf-8 -*-
#默认值参数需要注意的陷阱

print u'---------------#1. 默认值参数 Default Parameter Values---------------'

#1. 默认值参数 Default Parameter Values
#1.1 默认值参数的引入
#默认值参数的作用：还可以使用默认参数、可变参数和关键字参数，使得函数定义出来的接口，不但能处理复杂的参数，还可以简化调用者的代码。

#计算x的平方
def power(x):
	return x * x

#再定义一个计算n次方的函数时，上面的函数就失效了
def power(x, n):
    s = 1
    while n > 0:
        n -= 1
        s *= x
    return s
#print power(2) 报错，因为后面又定义了power(x, n)
print power(2, 10)

#使用默认函数可以解决这个问题
def power(x, n=2):
    s = 1
    while n > 0:
        n -= 1
        s *= x
    return s

print power(2)
print power(2, 10)

print u'-----------1.2 默认参数值陷阱————默认值参数必须指向不变对象------------'

#1.2 默认参数值陷阱————默认值参数必须指向不变对象
#定义一个函数，传入一个list，添加一个end后再返回
def addEnd(list=[]):
	list.append('END')
	return list
print addEnd([1, 2, 3])
#但是参数使用默认值时就会出问题，函数每次都“记住了”上次添加了'END'后的list。
print addEnd(), addEnd()

#解决办法：使用不变对象None
def add_END(list=None):
	if list is None:
		list = []
	list.append('END')
	return list
#现在，无论调用多少次，都不会有问题：
print add_END(), add_END()

