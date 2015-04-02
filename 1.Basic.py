#!/usr/bin/env python  
# -*- coding: utf-8 -*-
#1. Python2版本默认是ASCII编码，为了使其支持中文，需在文件开头加入coding=utf-8   

#2. 格式化输出
print 'Hi, %s, you have %d.' %('kesen', 1000000)

#3. 冒号后的制表符（默认4个空格）代表代码块
#打印绝对值:
a = -100
if a >= 0:
	print u'%d的绝对值是%d' %(a, a)
else:
	print u'%d的绝对值是%d' %(a, -a)

#4. 使用Unicode表示字符串，在字符串前面加u	
print u'我是中文'

#5. 逗号表示一个空格
print u'逗号', u'表示', u'一个空格'

#6. ASCII码与对应数字间转换
print u'A的ASCII码是%d' %(ord('A'))
print u'ASCII码65表示的字符是%c' %(chr(65))

#7. Unicode编码转换为UTF-8编码
str = u'中文'.encode('utf-8')
print str

print u'------------------------8. 可变数组 list-----------------------------'

#8. 可变数组 list
classmate = ['Michael', 'Bob', 'Tracy']
for i in range(0,len(classmate)):
	print classmate[i],
# len(classmate) -1 表示最后一个索引，也可以用-1表示。
print classmate[-1], classmate[-2], classmate[-3]
# 末尾追加元素
classmate.append('Adam')
print 'append(\'Adam\'):\n %s' %(classmate)
#插入
classmate.insert(1, 'Jack')
print 'insert(1, \'Jack\'):\n %s' %(classmate)
#删除最后一个元素
classmate.pop()
print 'pop():\n %s' %(classmate)
#删除指定位置的元素
classmate.pop(2)
print 'pop(2):\n %s' %(classmate)

print u'------------------------9. 不可变数组 tuplet----------------------------'

#9. 不可变数组 tuple
#tuple与list的区别在于tuple不可变
#Python中的不可变类型：string,integer,tuple
#Python中的可变类型：list,dict

classmate = ('Michael', 'Bob', 'Tracy')
#tuple只有一个元素时，可能与挂号冲突，用逗号消除歧义
t = (1,)
#tuple中含有List时，list的内容可以变化，因为tuple中指向list的指针指向并没有变
t = ('a', 'b', ['A', 'B'])
t[2][0] = 'a'
print id(t), t, id(t)  #24636592 ('a', 'b', ['a', 'B']) 24636592
#t[0] = 'c' #TypeError: 'tuple' object does not support item assignment
#print id(t), t

print u'------------------------10. 判断-------------------------------'

#10. 判断
age = 3
if age >= 18:
	print 'adult'
elif age >= 6:
	print 'teenager'
else:
	print 'kid'
	#kid

print u'------------------------11. 循环------------------------------'

#11. 循环
names = ['Michael', 'Bob', 'Tracy']
for name in names:
	print name,
	# Michael Bob Tracy

#12 range(i)函数:range函数用于生成一个[0, i)的整数序列
print '\n%s'%(range(5))
	#[0, 1, 2, 3, 4]

#13. 计算1~100的和
sum = 0
for i in range(101):
	sum += i
print sum
	# 5050

#14. 捕获用户输入函数raw_input()，它的返回值是一个字符串
birth = 0
while birth != -1:
	birth = int(raw_input())
	if birth < 2000: 
		print u'00后'
	else:
		print u'00前'
		
#15.字典dict
#字典是可变类型
dict = {'Michael':95, 'Bob':75, 'Tracy':85}
if 'Michael' in dict:
	print dict['Michael'], dict.get('Michael')
	print dict.pop('Bob'), dict
	#95 95
	#75 {'Michael': 95, 'Tracy': 85}

#16. 集合set
#set是一组key的集合，创建一个set，需要提供一个list作为输入集合：
set1 = set([1, 2])
#重复的元素会被自动过滤
set2 = set([1, 1, 2, 2, 3, 3])
print set2
	#set([1, 2, 3])
#添加、删除
set2.add(4)
set2.remove(4)
#两个set之间的交集和并集
print set1 & set2
print set1 | set2
	#set([1, 2])
	#set([1, 2, 3])

#17. 函数
def myAbs(x):
	if x >= 0:
		return x
	else:
		return -x
print myAbs(-1)
	#1
#pass表示占位符，可以用pass表示一个空函数
def myXXX():
	pass
	
#返回多个值。函数可以返回多个值吗？可以，实际上是通过返回的是一个tuple实现的。
#比如在游戏中经常需要从一个点移动到另一个点，给出坐标、位移和角度，就可以计算出新的新的坐标：
import math
def move(x, y, step, angle=0):
	nx = x + step * math.cos(angle)
	ny = y + step * math.sin(angle)
	return nx, ny
x, y = move(100, 100, 60, math.pi/6)
tuple  = move(100, 100, 60, math.pi/6)
print x, y
print tuple
	#151.961524227 130.0
	#(151.96152422706632, 130.0)
#原来返回值是一个tuple！但是，在语法上，返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，
#按位置赋给对应的值，所以，Python的函数返回多值其实就是返回一个tuple，但写起来更方便。

