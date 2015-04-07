#!/usr/bin/env python  
# -*- coding: utf-8 -*-

print u'-------------------------1. 序列化------------------------------'
#先尝试导入cPickle，如果失败，再导入pickle：
try:
	import cPickle as pickle
except ImportError:
	import pickle

#1.1 把一个对象序列化并写入文件
d = dict(name = 'Bob', age = 20, score = '88')
#1.1.1 pickle.dumps()方法把任意对象序列化成一个str
print pickle.dumps(d)  

