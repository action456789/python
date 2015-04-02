#!/usr/bin/env python  
# -*- coding: utf-8 -*-
#trap.py中介绍了默认参数，下面介绍可变参数

print u'------------------------1.可变参数-------------------------------'

#1.可变参数
#比如计算a2 + b2 + c2 + ……
#由于参数个数不确定，我们首先想到可以把a，b，c……作为一个list或tuple传进来，这样，函数可以定义如下：
def calc(numbers):
	sum = 0
	for num in numbers:
		sum += num * num
	return sum
#但是调用的时候，需要先组装出一个list或tuple：
print calc([1, 2, 3])
print calc((1, 2, 3))

#使用*号定义可变参数。在函数内部，参数numbers接收到的是一个tuple。
def calc2(*numbers):
	sum = 0
	for num in numbers:
		sum += num * num
	return sum	
#利用可变参数，调用函数的方式可以简化成这样：
print calc2(1, 2, 3)
print calc2() #0个参数也可以

#如果已经有一个list或者tuple，要调用一个可变参数怎么办？可以这样做：
nums = [1, 2, 3]
print calc2(nums[0], nums[1], nums[2])
print calc2(*nums) #这么写最简单，很常见的写法

print u'------------------------2. 关键字参数-------------------------------'

#2. 关键字参数
#可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
#而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。请看示例：
def person(name, age, **kw):
	print 'name: ', name, 'age: ', age, 'other: ', kw

#函数person除了必选参数name和age外，还接受关键字参数kw。在调用该函数时，可以只传入必选参数：
person('Michel', 30) #name:  Michel age:  30 other:  {}

#也可以传入任意个数的关键字参数：
person('Michel', 30, city='Beijing')
person('Michel', 30, city='Beijing', gender='M', job='Engineer')

#和可变参数类似，也可以先组装出一个dict，然后，把该dict转换为关键字参数传进去：
kw = {'city': 'Beijing', 'job': 'Engineer'}
person('Michel', 30, **kw)

print u'------------------------3. 参数组合-------------------------------'

#3. 参数组合
#多种参数一起使用时，参数定义的顺序必须是：必选参数、默认参数、可变参数和关键字参数。

print u'------------------------4.递归函数-------------------------------'

#4.递归函数
#计算阶乘n! = 1 x 2 x 3 x ... x n，用函数fact(n)表示。可以看出：
#fact(n) = n! = 1 x 2 x 3 x ... x (n-1) x n = (n-1)! x n = fact(n-1) x n
#所以，fact(n)可以表示为n x fact(n-1)，只有n=1时需要特殊处理。
#于是，fact(n)用递归的方式写出来就是：
def fact(n):
	if n == 1:
		return 1
	return n * fact(n-1)
print fact(5)

# 使用reduce函数实现
def multip(x, y):
	return x * y
print reduce(multip, range(1, 6))

print u'------------------------5.切片-------------------------------'

#5.切片
#切片用于取一个list或tuple的部分元素
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print L[0:3]  #取索引为0，1，2的三个元素
#如果第一个索引是0，可以省略
print L[:3]
#倒数切片：取倒数第一个和倒数第二个元素
print L[-2:]  #['Bob', 'Jack']
#每两个取一个
print L[0:5:2]  #['Michael', 'Tracy', 'Jack']
#可以简写为
print L[::2]

#tuple也可进行切片操作，只是原tuple不变，返回一个新的tuple
t = (1, 2, 3, 4, 5) 
print t[:3]  #(1, 2, 3)
print t  #(1, 2, 3, 4, 5)

#字符串也可以进行切片操作，只是原字符串不变
print 'ABCDEF'[:3]

print u'------------------------#6.迭代-------------------------------'

#6.迭代
#如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们称为迭代（Iteration）。

#6.1字典的迭代

#迭代字典的Key
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
	print key,
#迭代字典的Value
for value in d.itervalues():
	print value,
print '\n'
#同时迭代Key和Value
for key, value in d.iteritems():
	print key, value

#6.2 字符串的迭代
for ch in 'ABCDEF':
	print ch,
print '\n'

#6.3 判断一个对象是否可迭代
#如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断
from collections import Iterable
print isinstance('abc', Iterable) #True
print isinstance(123, Iterable) # False

#6.4 取list得下标
#Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身
for i, value in enumerate(['A', 'B', 'C']):
	print i, value
#上面的for循环里，同时引用了两个变量，在Python里是很常见的，比如下面的代码：
for x, y in [(1, 1), (2, 4), (3, 9)]:
	print x, y
	
print u'------------------------#7.列表生成式-------------------------------'

#7.列表生成式 List Comprehension

#7.1 常用的列表生成式
#例如，要生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]可以用:
print range(1, 11)
#但如果要生成[1x1, 2x2, 3x3, ..., 10x10]怎么做？
print [x*x for x in range(1, 10)]
#for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方：
print [x*x for x in range(1, 10) if x%2 == 0]
#还可以使用两层循环，可以生成全排列：
print [m + n for m in 'ABC' for n in 'XYZ']

#7.1 列出当前目录下的所有文件和目录名，可以通过一行代码实现
import os #导入os模块
print [d for d in os.listdir('.')] #os.listdir可以列出文件和目录

print u'------------------------#8.生成器-------------------------------'

#8.生成器

#通过列表生成式可以生成完整的列表，当列表很大是需要很大内存空间。
#如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？
#这样就不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器（Generator）。

#8.1 创建方法1：第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator：
L = [x*x for x in range(10) ]
g = (x*x for x in range(10))
print L #[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print g #<generator object <genexpr> at 0x016DEF30>

#8.1.1 访问Generrator中的元素
#每次调用next都访问下一个元素
print g.next(), g.next(), g.next()  #0 1 4
for n in g:
	print n,  
#9 16 25 36 49 64 81

#8.2 创建方法2：函数定义中包含 yield 关键字
#例如，著名的斐波拉契数列（Fibonacci），除第一个和第二个数外，任意一个数都可由前两个数相加得到：
#1, 1, 2, 3, 5, 8, 13, 21, 34, ...
#使用普通的函数实现：
def fib(max):
	n, a, b = 0, 0, 1
	while n < max:
		print b,
		a, b = b, a + b
		n += 1
print '\n', fib(10)
#把fib函数变成generator，只需要把print b改为yield b就可以了
def fib(max):
	n, a, b = 0, 0, 1
	while n < max:
		yield b,
		a, b = b, a + b
		n += 1
print '\n', fib(10)

for n in fib(10):
	print n

#8.3 generator与函数的区别
#generator和函数的执行流程不一样。函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
#而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
def odd():
	print 'step 1'
	yield 1
	print 'step 2'
	yield 3
	print 'step 3'
	yield 5
odd = odd()
print odd.next()
print odd.next()
print odd.next()
# print odd.next() #没有yield可以执行了
