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


print u'-------------------------5. XML------------------------------'
#操作XML有两种方法：DOM和SAX。DOM会把整个XML读入内存，解析为树，因此占用内存大，解析慢，
#优点是可以任意遍历树的节点。SAX是流模式，边读边解析，占用内存小，解析快，缺点是我们需要自己处理事件。

#正常情况下，优先考虑SAX，因为DOM实在太占内存。
#在Python中使用SAX解析XML非常简洁，通常我们关心的事件是start_element，end_element和char_data，准备好这3个函数，然后就可以解析xml了。

#当SAX解析器读到一个节点:<a href="/">python</a> 时，会产生3个事件：

#1. start_element事件，在读取<a href="/">时；
#2. char_data事件，在读取python时；
#3. end_element事件，在读取</a>时。

from xml.parsers.expat import ParserCreate

class DefaultSaxHandler(object):
	def start_element(self, name, attrs):
		print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))

	def char_data(self, text):
		print('sax:char_data: %s' % text)

	def end_element(self, name):
		print('sax:end_element: %s' % name)

xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''

handler = DefaultSaxHandler()
parser = ParserCreate()
parser.returns_unicode = True
parser.StartElementHandler = handler.start_element
parser.CharacterDataHandler = handler.char_data
parser.EndElementHandler = handler.end_element

parser.Parse(xml)

#当设置returns_unicode为True时，返回的所有element名称和char_data都是unicode，处理国际化更方便。
#需要注意的是读取一大段字符串时，CharacterDataHandler可能被多次调用，所以需要自己保存起来，在EndElementHandler里面再合并。

print u'------------------------- 6. HTMLParser ------------------------------'
# HTML本质上是XML的子集，但是HTML的语法没有XML那么严格，所以不能用标准的DOM或SAX来解析HTML。
# 好在Python提供了HTMLParser来非常方便地解析HTML，只需简单几行代码：

from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint

class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print('<%s>' % tag)

    def handle_endtag(self, tag):
        print('</%s>' % tag)

    def handle_startendtag(self, tag, attrs):
        print('<%s/>' % tag)

    def handle_data(self, data):
        print('data')

    def handle_comment(self, data):
        print('<!-- -->')

    def handle_entityref(self, name):
        print('&%s;' % name)

    def handle_charref(self, name):
        print('&#%s;' % name)

parser = MyHTMLParser()
parser.feed('<html><head></head><body><p>Some <a href=\"#\">html</a> tutorial...<br>END</p></body></html>')

# feed()方法可以多次调用，也就是不一定一次把整个HTML字符串都塞进去，可以一部分一部分塞进去。

# 特殊字符有两种，一种是英文表示的&nbsp;，一种是数字表示的&#1234;，这两种字符都可以通过Parser解析出来