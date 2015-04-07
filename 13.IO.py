#!/usr/bin/env python  
# -*- coding: utf-8 -*-

print u'-------------------------IO编程------------------------------'

#下面所讲的都是同步方式读写文件

print u'----------------1. 读 ASCII 编码的文本文件-----------------------'
print u'----------------1.1 一次性全部读完（文件很小时）------------------'
f = open('hello.py', 'r')  
try:
	text = f.read() 
	print text
finally:
	f.close()


print u'----------------1.2 每次读一行，直到读完所有行（文件很大时）--------'
f = open('hello.py', 'r')  
for line in f.readlines():
	print(line.strip())  # 把末尾的'\n'删掉

print u'----------------1.3 简单的写法，本质与1.1是一样的------------'
with open('hello.py', 'r') as f:
	print f.read()


print u'----------------2. 读二进制文件（图片、视频等）---------------------'


print u'----------------3. 读非 ASCII 编码的文本文件-----------------------'
#要读取非ASCII编码的文本文件，就必须以二进制模式打开，再解码。比如GBK编码的文件：
f = open('hello.py', 'rb')
u = f.read().decode('gbk')


print u'----------------3.1 简单的写法------------'
import codecs
with codecs.open('hello.py', 'r', 'gbk') as f:
	f.read()


print u'----------------4 写文件------------'
f = open('test.txt', 'w') #写二进制文件用wb
try:
	f.write('hello world!\n')
finally:
	f.close() #这时才会写入文件

with open('test.txt', 'r') as f:
	print f.read()

print u'----------------4.1 简单的写法------------'
with open('test.txt', 'a') as f: #追加写文件
	f.write('hello world!\n')

with open('test.txt', 'r') as f:
	print f.read()

print u'----------------2. file-like Object---------------------'
#像open()函数返回的这种有个read()方法的对象，在Python中统称为file-like Object。
#除了file外，还可以是内存的字节流，网络流，自定义流等等。file-like Object不要求从特定类继承，只要写个read()方法就行。
#StringIO就是在内存中创建的file-like Object，常用作临时缓冲。