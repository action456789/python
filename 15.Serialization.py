#!/usr/bin/env python  
# -*- coding: utf-8 -*-

import os
abspath = os.path.abspath('.')

print u'-------------------------1. 序列化------------------------------'
#先尝试导入cPickle，如果失败，再导入pickle：
try:
	import cPickle as pickle
except ImportError:
	import pickle

#1.1 把一个对象序列化并写入文件
d = dict(name = 'Bob', age = 20, score = '88')

#1.1.1 pickle.dumps()方法把任意对象序列化成一个str，然后，就可以把这个str写入文件
print pickle.dumps(d)  

#1.1.2 或者用另一个方法pickle.dump()直接把对象序列化后写入一个file-like Object：
path = os.path.join(abspath, 'testdir') #D:\ks\github\python\testdir
if not os.path.exists(path):
	os.mkdir(path)
dataFile = os.path.join(path, 'dump.txt') #D:\ks\github\python\testdir\dump.txt

f = open(dataFile, 'wb')
pickle.dump(d, f)
f.close()


print u'-------------------------2. 反序列化------------------------------'
f = open(dataFile, 'rb')
data = pickle.load(f)
f.close()
print data

print u'-------------------------3. JSON------------------------------'
#3.1 把Python对象变成一个JSON
#dumps()方法返回一个str，内容就是标准的JSON。类似的，dump()方法可以直接把JSON写入一个file-like Object。
import json
print json.dumps(d)

#3.2 把JSON反序列化为Python对象
#用loads()或者对应的load()方法，前者把JSON的字符串反序列化，后者从file-like Object中读取字符串并反序列化：
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print json.loads(json_str)

print u'-------------------------4. JSON 序列化自定义对象------------------------------'
from Student import Student
s1 = Student('Bob', 20, 88)

#4.1 使用类的自定义的序列化函数进行序列化
print json.dumps(s1, default = Student.student2dict)

#4.2 使用类的 __dict__ 进行序列化
#下次如果遇到一个Teacher类的实例，照样无法序列化为JSON。我们可以偷个懒，把任意class的实例变为dict：
#因为通常class的实例都有一个__dict__属性，它就是一个dict，用来存储实例变量。也有少数例外，比如定义了__slots__的class。
print json.dumps(s1, default = lambda obj: obj.__dict__)

#4.3 JSON 反序列化为对象

def dict2student(d):
	return Student(d['name'], d['age'], d['score'])
#loads()方法首先转换出一个dict对象，然后，我们传入的object_hook函数负责把dict转换为Student实例：
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print json.loads(json_str, object_hook = dict2student)

