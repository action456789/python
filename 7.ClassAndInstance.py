#!/usr/bin/env python  
# -*- coding: utf-8 -*-

print u'---------------1.类和实例---------------'

#python中所有的类都是继承自object

#实例的变量名如果以__开头，就变成了一个私有变量（private）

class Student(object):
	def __init__(self, name, score, height):
		super(Student, self).__init__()
		self.__name = name
		self.__score = score
		self.height = height

	def getName(self):
		return self.__name

	def getScore(self):
		return self.__score

	def height(self, height):
		self.height = height

	def printStudent(self):
		print 'name: %s, score: %s, height: %d' %(self.__name, self.__score, self.height)

s1 = Student('Jack', 98, 170)
s1.printStudent();

#以一个下划线开头的实例变量名，比如_name，这样的实例变量外部是可以访问的，
#但是，按照约定俗成的规定，当你看到这样的变量时，意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”。

print u'---------------2.继承和多态---------------'

class Animal(object):
	def run(self):
		print 'Animal is running'

class Dog(Animal):
	def run(self):
		print 'Dog is running'

class Cat(Animal):
	def run(self):
		print 'Cat is running'

class Hasky(Dog):
	def run(self):
		print 'Hasky is running'

animal = Animal()
animal.run()

dog = Dog()
dog.run()

cat = Cat()
cat.run()		

hasky = Hasky()
hasky.run()

print u'--------------- 3.type() ---------------'

#3.1 使用type()
print type(123)
print type('123')
print type(abs)
print type(Student)

#3.2 判断是不是某种类型：
import types
print type('abc') == types.StringType
print type(u'anc') == types.UnicodeType
print type([]) == types.ListType
print type(str) == types.TypeType  #所有类型本身的类型就是TypeType

print u'--------------- 4.isinstance() ---------------'		

#对于class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数。
print isinstance(dog, Dog)
print isinstance(dog, Animal)
print isinstance(hasky, Hasky)

#能用type()判断的基本类型也可以用isinstance()判断：
print isinstance('a', str)

#判断是否是str或者unicode:
print isinstance('a', (str, unicode))
print isinstance(u'a', (str, unicode))

#由于str和unicode都是从basestring继承下来的，所以，还可以把上面的代码简化为：
#print isinstance(u'a', basestring)

print u'--------------- 5.dir()、hasattr()、setattr()---------------'		

#如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list
print dir('abc')

#类似__xxx__的属性和方法在Python中都是有特殊用途的，比如__len__方法返回长度。在Python中，如果你调用len()函数
#试图获取一个对象的长度，实际上，在len()函数内部，它自动去调用该对象的__len__()方法，所以，下面的代码是等价的：
print len('abc')
print 'abc'.__len__()

#我们自己写的类，如果也想用len(myObj)的话，就自己写一个__len__()方法：
class MyObject(object):
	def __init__(self):
		self.x = 9

	def power(self):
		return self.x * self.x

	def __len__(self):
		return 100

obj = MyObject()
print len(obj)

print hasattr(obj, 'x')  # 有属性'x'吗？

if not hasattr(obj, 'y'):
	setattr(obj, 'y', 19)  # 设置一个属性'y'，初值为19
	print obj.y

#如果试图获取不存在的属性，会抛出AttributeError的错误：
# getattr(obj, 'z') #AttributeError: 'MyObject' object has no attribute 'z'

#可以传入一个default参数，如果属性不存在，就返回默认值：
print getattr(obj, 'z', 404)  # 获取属性'z'，如果不存在，返回默认值404

#也可以获得对象的方法：
print hasattr(obj, 'power')
fn = getattr(obj, 'power')
print fn()
