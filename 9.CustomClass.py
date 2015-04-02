#!/usr/bin/env python  
# -*- coding: utf-8 -*-

print u'---------------定制类---------------'
print u'-----------------------------1. __str__------------------------------'

#__str__的作用与Objective-C的descript函数类似，用于打印一个类和对象的信息
#__str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的。

class Student(object):
	def __init__(self, name):
		self.name = name
	def __str__(self):
		return 'Student object (name: %s)' %(self.name)
	__repr__ = __str__

s = Student('Michael')
print s

print u'-------------------------------2. __iter__--------------------------------'
#如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象，
#然后，Python的for循环就会不断调用该迭代对象的next()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环。

#我们以斐波那契数列为例，写一个Fib类，可以作用于for循环：
class Fib(object):
	def __init__(self):
		self.a, self.b = 0, 1  # 初始化两个计数器a，b

	def __iter__(self):
		return self  # 实例本身就是迭代对象，故返回自己

	def next(self):
		self.a, self.b = self.b, self.a + self.b # 计算下一个值
		if self.a > 10000: #退出条件
			raise StopIteration()
		return self.a

for n in Fib():
	print n,

print u'----------------------------3. __getitem__--------------------------'
#上面的Fib类，如果要表现得像list那样按照下标取出元素，需要实现__getitem__()方法：
class Fib(object):
	def __getitem__(self, n):
		a, b = 1, 1
		for x in range(n):
			a, b = b, a+b
		return a

f = Fib()
print f[1], f[2], f[3], f[10]

#但是list有个神奇的切片方法：
print range(100)[5 : 10]

#对于Fib却报错。原因是__getitem__()传入的参数可能是一个int，也可能是一个切片对象slice，所以要做判断：
class Fib(object):
	def __getitem__(self, n):
		if isinstance(n, int):
			a, b = 1, 1
			for x in range(n):
				a, b = b, a+b
			return a
		
		if isinstance(n, slice):
			start = n.start
			stop = n.stop
			a, b = 1, 1
			L = []

			for x in range(stop):
				if x >= start:
					L.append(a)
				a, b = b, a+b

			return L

f = Fib()
print f[0:5]

#也没有对负数作处理，所以，要正确实现一个__getitem__()还是有很多工作要做的。

#此外，如果把对象看成dict，__getitem__()的参数也可能是一个可以作key的object，例如str。

#与之对应的是__setitem__()方法，把对象视作list或dict来对集合赋值。最后，还有一个__delitem__()方法，用于删除某个元素。

print u'----------------------------4. __getattr__--------------------------'
#__getattr__()方法，用于动态返回一个属性。
class Student(object):
	def __init__(self):
		self.name = 'Michael'

	#动态返回一个属性
	def __getattr__(self, attr):
		if attr == 'score':
			return 99
		#动态返回一个函数也是可以的
		if attr == 'age':
			return lambda:25

		#其他属性，抛出错误
		raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)
		
#当调用不存在的属性时，比如score，Python解释器会试图调用__getattr__(self, 'score')来尝试获得属性，
#这样，我们就有机会返回score的值,已有的属性，比如name，不会在__getattr__中查找
s = Student()
print s.score
print s.age()

print u'----------------------------5. __call__--------------------------'
#实现__call__方法可以直接对实例本身进行调用,这样你就可以把对象看成函数了：
class Student(object):
	def __init__(self, name):
		self.name = name
	def __call__(self):
		print 'My name is %s.' %(self.name) 

s = Student('Michael')
s()

#__call__()还可以定义参数。对实例进行直接调用就好比对一个函数进行调用一样，
#所以你完全可以把对象看成函数，把函数看成对象，因为这两者之间本来就没啥根本的区别。

#判断一个对象是否能被调用，能被调用的对象就是一个Callable对象：
print callable(s)
print callable([1, 2, 3])