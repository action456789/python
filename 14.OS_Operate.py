#!/usr/bin/env python  
# -*- coding: utf-8 -*-

print u'-------------------------1. 获取操作系统信息------------------------------'
import os
print os.name # 操作系统名字
#如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。

#要获取详细的系统信息，可以调用uname()函数（windows上没有这个函数）：
if os.name == 'posix':
	print os.uname()


print u'-------------------------2. 获取环境变量------------------------------'
print os.environ #类型是dict

print '\n'
#要获取某个环境变量的值，可以调用os.getenv()函数：
print os.getenv('PATH')


print u'-------------------------3. 操作文件和目录------------------------------'
#3.1 当前目录的绝对路径
print u'当前目录的绝对路径: %s' %(os.path.abspath('.'))

#3.2 在某个目录下创建一个新目录
#3.2.1 新目录完整路径
abspath = os.path.abspath('.')  #windows下为：D:\ks\github\python， Linux/Unix/Mac下为D:/ks/github/python
path = os.path.join(abspath, 'testdir') #拼接路径，Windows下为D:\ks\github\python\testdir，Linux/Unix/Mac下为D:/ks/github/python/testdir
#3.2.2 创建目录D:\ks\github\python\testdir
if not os.path.exists(path):  #路径不存在时创建
	os.mkdir(path)

#3.3 删除目录
#os.rmdir(path)

#3.4 拆分路径
print os.path.split(path) #('D:\\ks\\github\\python', 'testdir')

#3.5 拷贝路径/文件
#3.5.1 #copyfile函数所在模块
import shutil
#3.5.2 创建test.txt
if not os.path.exists('test.txt'):
	with open('test.txt', 'w') as f: 
		pass
src = os.path.join(abspath, 'test.txt')
dst = os.path.join(path, 'test.txt')
shutil.copyfile(src, dst)

#3.5 获取扩展名
print os.path.splitext('test.txt') #('test', '.txt')

#3.6 重命名
os.rename('test.txt', 'test.py')

#3.7 删除文件
os.remove('test.py')


print u'-------------------------4. 过滤文件------------------------------'
#4.1 列出当前目录下的所有目录
print [d for d in os.listdir('.') if os.path.isdir(d)]

#4.2 列出所有.py 文件
print [py for py in os.listdir('.') if os.path.isfile(py) and os.path.splitext(py)[1] == '.py']
