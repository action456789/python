#!/usr/bin/env python  
# -*- coding: utf-8 -*-

print u'---------------1.函数作为返回值---------------'
print u'-------------1.1. 将函数作为返回值，可以需要时再执行函数-------------'

#· 高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。
#我们来实现一个可变参数的求和。通常情况下，求和的函数是这样定义的：
def calcSum(*args):
	sum = 0
	for n in args:
		sum += n
	return sum

#但是，如果不需要立刻求和，而是在后面的代码中，根据需要再计算怎么办？可以不返回求和的结果，而是返回求和的函数！
def lazySum(*args):
	def sum():
		sum = 0
		for n in args:
			sum += n
		return sum 
	return sum #当lazySum返回函数sum时，相关参数和变量都保存在返回的函数中

f = lazySum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print f #返回求和函数
print f() #返回求和结果

#当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数：
f1 = lazySum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print f == f1

print u'--------1.2. 返回函数不要引用任何循环变量，或者后续会发生变化的变量。--------'
def count():
	fs = []
	for i in range(1, 4):
		def f():
			return i * i
		fs.append(f) #将函数放入fs中
	return fs

f1, f2, f3 = count()

#在上面的例子中，每次循环，都创建了一个新的函数，然后，把创建的3个函数都返回了。
#你可能认为调用f1()，f2()和f3()结果应该是1，4，9，但实际结果是：
print f1(), f2(), f3()

#全部都是9！原因就在于返回的函数引用了变量i，但它并非立刻执行。
#等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9。

print u'---------------1.3.如果一定要引用循环变量怎么办？---------------'
#方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变：
def count():
	fs = []
	for i in range(1, 4):
		def f(j):
			def g():
				return j * j
			return g
		fs.append(f(i))
	return fs

f1, f2, f3 = count()
print f1(), f2(), f3()

#缺点是代码较长，可利用lambda函数缩短代码。下面介绍lambda

print u'---------------2.匿名函数 lambda ---------------'
#当我们在传入函数时，有些时候，不需要显式地定义函数，直接传入匿名函数更方便。

#以map()函数为例，计算f(x)=x2时，除了定义一个f(x)的函数外，还可以直接传入匿名函数：
print map(lambda x: x * x, range(1, 10))

#· 关键字lambda表示匿名函数，冒号前面的x表示函数参数。
#· 匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。

#· 用匿名函数有个好处，因为函数没有名字，不必担心函数名冲突。
#· 此外，匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数：
f = lambda x: x * x
print f, f(5)

print u'---------------3.装饰器 ---------------'
print u'---------------3.1 函数对象的 __name__ ---------------'

#函数也是一个对象
def now():
	print u'2015年3月31日'
f = now
f()
print f.__name__, now.__name__

print u'-----------3.2 装饰器（Decorator）:在运行时增加函数功能 -----------'
#· 现在，假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义，
#· 这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
#· 本质上，decorator就是一个参数为一个函数，返回值也为一个函数的高阶函数。

print u'-----------3.2.1 无参数装饰器 -----------'
#所以，我们要定义一个能打印日志的decorator，可以定义如下：
def log(func):
	def wrapper(*args, **kw): #参数定义是(*args, **kw)，因此，wrapper()函数可以接受任意参数的调用。
		print 'call %s():' %func.__name__
		return func(*args, **kw)
	return wrapper


#我们要借助Python的@语法，把decorator置于函数的定义处：
@log
def now():
	print u'2015年3月31日'

now()  #相当于now = log(now)

print u'--调用过程如下：--'
f1 = log(now)
f1()

print u'-----------3.2.2 含参数装饰器 -----------'
#如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数，写出来会更复杂。
#比如，要自定义log的文本：
def log(text):
	def decorator(func):
		def wrapper(*args, **kw):
			print '%s %s():' % (text, func.__name__)
			return func(*args, **kw)
		return wrapper
	return decorator

@log('execute')
def now():
	print u'2015年3月31日'

now() #相当于now = log('execute')(now)

print u'--调用过程如下：--'
f1 = log('execute')
f2 = f1(now)
f2()

print u'-----------3.2.3 最后一步：使用 functools.wraps -----------'
#在上面的代码中，但还差最后一步。
#因为我们讲了函数也是对象，它有__name__等属性，但你去看经过decorator装饰之后的函数，
#它们的__name__已经从原来的'now'变成了'wrapper'，
print now.__name__

#所以，一个完整的decorator的写法如下：
import functools
def log(func):
	@functools.wraps(func)
	def wrapper(*args, **kw):
		print 'call %s():' %func.__name__
		return func(*args, **kw)
	return wrapper

@log
def now():
	print u'2015年3月31日'

now()
print now.__name__

#或者含参数的decorator
import functools
def log(text):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args, **kw):
			print '%s %s():' % (text, func.__name__)
			return func(*args, **kw)
		return wrapper
	return decorator

@log('execute')
def now():
	print u'2015年3月31日'
now()
print now.__name__

print u'----------------------4. 偏函数 -----------------------'
#Python的functools模块提供了很多有用的功能，其中一个就是偏函数（Partial function）。
#偏函数的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。

#例如：
#Python的ini()函数可以把字符串转换为整数，默认按10进制转换
print int('12345')
#如果传入参数base，可以按N进制转
print int('12345', 8)

#我们可以定义自己的转换为2进制的函数：
def int2(x, base = 2):
	return int(x, base)

#更简单的方式是利用偏函数
import functools
int2 = functools.partial(int, base = 2)
print int2('100000')