#!/usr/bin/env python  
# -*- coding: utf-8 -*-

print u'-------------------------IO编程------------------------------'

#下面所讲的都是同步方式读写文件

print u'-------------------------读文件-----------------------------'

#繁琐的写法
f = open('hello.py')  
try:
	text = f.read() 
	print text
finally:
	f.close()

#简单的写法，本质与上面是一样的
with open('hello.py') as f:
	print f.read()

