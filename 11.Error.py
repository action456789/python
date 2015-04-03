#!/usr/bin/env python  
# -*- coding: utf-8 -*-

print u'-----------------------------try, except, else, finally------------------------------'

try:
	print 'try...'
	r = 10 / int('a')
	print 'result: ', r

except ValueError, e:
	print 'ValueError:', e

except ZeroDivisionError, e:
	print 'except:', e

else: #当没有错误发生时，会自动执行else语句
	print 'no error!'

finally: #无论有没有错误发生，finally都会执行
	print 'finally...'

print 'END'

print u'-------------------------只会捕获父类的错误------------------------------'

#如果try中的代码出错，会执行对应的错误 except 中的代码，然后执行 finally 中的代码
#如果try中的代码没出错，会执行 try 中的代码， 然后执行 finally 中的代码

#Python的错误其实也是class，所有的错误类型都继承自BaseException，
#所以在使用except时需要注意的是，它不但捕获该类型的错误，还把其子类也“一网打尽”。比如：

try:
	foo()

except StandardError, e:
	print 'StandardError'

except ValueError, e: #ValueError是StandardError的子类，所以这个错误永远捕获不到
	print 'ValueError'

print u'-------------------------错误可以跨层处理------------------------------'

#比如函数main()调用foo()，foo()调用bar()，结果bar()出错了，这时，只要main()捕获到了，就可以处理：
def foo(s):
	return 10/int(s)
def bar(s):
	return foo(s)/2
def main():
	try:
		bar('0')
	except StandardError, e:
		print 'Error!'
	finally:
		print 'finally...'

main()
#也就是说，不需要在每个可能出错的地方去捕获错误，
#只要在合适的层次去捕获错误就可以了。这样一来，就大大减少了写try...except...finally的麻烦。

print u'-------------------------调用堆栈------------------------------'

#如果错误没有被捕获，它就会一直往上抛，最后被Python解释器捕获，打印一个错误信息，然后程序退出
def main():
	bar('0')

#main()

print u'-------------------------获取调用堆栈：logging------------------------------'

#如果不捕获错误，自然可以让Python解释器来打印出错误堆栈，但程序也被结束了。
#既然我们能捕获错误，就可以把错误堆栈打印出来，然后分析错误原因，同时，让程序继续执行下去。
import logging

def main():
	try:
		bar('0')
	except StandardError, e:
		logging.exception(e)
main()

print u'-------------------------抛出错误实例------------------------------'

#定义一个错误的class，选择好继承关系，然后，用raise语句抛出一个错误的实例：
class FooError(StandardError):
	pass
def foo(s):
	n = int(s)
	if n == 0:
		raise FooError('invalid value: %s' %s)
	return 10/s

#foo(0)
#只有在必要的时候才定义我们自己的错误类型。如果可以选择Python已有的内置的错误类型
#（比如ValueError，TypeError），尽量使用Python内置的错误类型。

print u'-------------------------在 except 中抛出错误------------------------------'

#这是一种常见的错误处理方式
#如果当前函数不知道如何处理错误，最恰当的方式是继续往上抛，让顶层调用者去处理。

def foo(s):
	return 10 / int(s)
def bar(s):
	try:
		return foo(s) * 2
	except StandardError, e:
		print 'error!'
		raise #raise语句如果不带参数，就会把当前错误原样抛出
def main():
	bar(0)

#main()

#在except中raise一个Error，还可以把一种类型的错误转化成另一种类型：
try:
	10 / 0
except ZeroDivisionError:
	raise ValueError('input error!')

#只要是合理的转换逻辑就可以，但是，决不应该把一个IOError转换成毫不相干的ValueError。