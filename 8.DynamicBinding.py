#!/usr/bin/env python  
# -*- coding: utf-8 -*-

print u'---------------1.实例的动态绑定---------------'

#Python是动态语言，创建了一个class的实例后，我们可以给该实例绑定任何属性和方法。
class Student(object):
	pass

#1.1 给实例绑定一个属性
s1 = Student()
s1.name = 'Michael'
print s1.name

#1.2 给实例绑定一个方法
def setAge(self, age): 
	self.age = age

from types import MethodType
s1.setAge = MethodType(setAge, s1, Student) # 给实例绑定一个方法
s1.setAge(18)
print s1.age

#但是，给一个实例绑定的方法，对另一个实例是不起作用的

#1.3 给类绑定方法————相当于给所有的实例绑定了方法
def setScore(self, score):
	self.score = score
Student.setScore = MethodType(setScore, None, Student)
s2 = Student()
s2.setScore(100)
s1.setScore(98)
print s1.score, s2.score

print u'---------------2.__slots__---------------'

#使用__slots__对类的属性进行限制，例如只允许对Student实例添加name和age属性。
#为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class能添加的属性：
class Student(object):
	__slots__ = ('name', 'age') #用tuple定义允许绑定的属性名称

s = Student()
s.name = 'Michael'
# s.score = '99' #'Student' object has no attribute 'score'


#__slots__定义的属性仅对当前类起作用，对继承的子类是不起作用的：


print u'---------------3.使用@property---------------'
#类比一下OC，OC的property可以把点调用转换为get/set方法的调用，Python也类似
#Python中property的本质是装饰器

#先看不使用property的类
class Student(object):
	def getScore(self):
		return self._score
	def setScore(self, value):
		if not isinstance(value, int):
			raise ValueError('score must bu an integer')
		if value <= 0 or value >= 100:
			raise ValueError('score must between 0~100')
		self._score = value

s = Student()
#s.setScore(200)  #error
#还是可以使用点语法随便赋值
s.score = 200

#使用property
class Student(object):
	@property
	def score(self):
		return self._score

	@score.setter
	def score(self, value):
		if not isinstance(value, int):
			raise ValueError('score must bu an integer')
		if value <= 0 or value >= 100:
			raise ValueError('score must between 0~100')
		self._score = value

	@property
	def isPass(self):
		return self._score >= 60 #只读属性

s = Student()
#s.score = 200  #error

#注意到这个神奇的@property，我们在对实例属性操作的时候，就知道该属性很可能不是直接暴露的，而是通过getter和setter方法来实现的。
#还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性：
s.score = 88
print s.isPass