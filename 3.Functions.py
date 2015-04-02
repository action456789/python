#!/usr/bin/env python  
# -*- coding: utf-8 -*-

print u'------------------------1. 高阶函数-----------------------------'

#1. 高阶函数 Higher-order function
#高阶函数：一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数。
#比如：
def add(x, y, f):
	return f(x) + f(y)

print add(-5, 6, abs) #11

print u'------------------------2. map()-----------------------------'

#2. map()
#map()函数接收两个参数，一个是函数，一个是序列，map将传入的函数依次作用到序列的每个元素，并把结果作为新的list返回。

#2.1 举例说明，比如我们有一个函数f(x)=x2，要把这个函数作用在一个list [1, 2, 3, 4, 5, 6, 7, 8, 9]上，就可以用map()实现如下：
def f(x):
	return x * x
print map(f, range(1, 10))

#2.2 再例如：把这个list所有数字转为字符串：
print map(str, range(1, 10))

print u'------------------------3. reduce()-----------------------------'

#3. reduce()
# reduce把一个函数作用在一个序列[x1, x2, x3...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

#3.1 比方说对一个序列求和，就可以用reduce实现：
def add(x, y):
	return x + y
print reduce(add, range(1, 10))

#当然求和运算可以直接用Python内建函数sum()，没必要动用reduce。
print sum(range(1, 10))

#3.2 str转换为int 
# 字符串str也是一个序列，对上面的例子稍加改动，配合map()，我们就可以写出把str转换为int的函数：
def fn(x, y):
	return x * 10 + y

def char2num(s):
	return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

print map(char2num, '1245678')
print reduce(fn, map(char2num, '12345678'))

#整理成函数就是:
def str2int(s):
	def fn(x, y):
		return x * 10 + y
	def char2num(s):
		return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
	return reduce (fn, map(char2num, s))

print u'------------------------4. filter()-----------------------------'

#4. filter() 过滤器
#Python内建的filter()函数用于过滤序列。
#filter()接收一个函数和一个序列,把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。

#例如：在一个list中，删掉偶数，只保留奇数：
def isOdd(n):
	return n % 2 == 1
print filter(isOdd, range(0,10))

print u'------------------------5. sorted()-----------------------------'

#5. sorted() 排序算法
#通常规定，对于两个元素x和y，如果认为x < y，则返回-1，如果认为x == y，则返回0，如果认为x > y，则返回1

#5.1 Python内置的sorted()函数就可以对list进行排序：
print sorted([36, 5, 12, 9, 21]) #[5, 9, 12, 21, 36]

#5.2 sorted()函数也是一个高阶函数，它还可以接收一个比较函数来实现自定义的排序。
#比如，如果要倒序排序，我们就可以自定义一个reversedCmp函数：
def reversedCmp(x, y):
	if x > y:
		return -1
	if x < y:
		return 1
	return 0
print sorted([36, 5, 12, 9, 21], reversedCmp) #[36, 21, 12, 9, 5]
 
#5.3 字符串排序
#默认情况下，对字符串排序，是按照ASCII的大小比较的，由于'Z' < 'a'，结果，大写字母Z会排在小写字母a的前面。
print sorted(['bob', 'about', 'Zoo', 'Credit']) #['Credit', 'Zoo', 'about', 'bob']

#当我们需要忽略大小写的排序时，只要定义忽略大小写的比较算法即可
def cmp_ignore_case(s1, s2):
    u1 = s1.upper()
    u2 = s2.upper()
    if u1 < u2:
        return -1
    if u1 > u2:
        return 1
    return 0
print sorted(['bob', 'about', 'Zoo', 'Credit'], cmp_ignore_case)  #['about', 'bob', 'Credit', 'Zoo']

