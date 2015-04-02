#!/usr/bin/env python  
# -*- coding: utf-8 -*-
print u'-----------------------------使用元类------------------------------'

print u'-----------------------------1. 使用 type() 函数动态创建类------------------------------'

from hello import Hello #导入hello模块的Hello
h = Hello()
h.hello()

#当Python解释器载入hello模块时，就会依次执行该模块的所有语句，执行结果就是动态创建出一个Hello的class对象，测试如下：

print type(Hello) #<type 'type'>
print type(h) #<class 'hello.Hello'>

#type()函数既可以返回一个对象的类型，又可以创建出新的类型，比如，我们可以通过type()函数创建出Hello类：
def fn(self, name='world'): # 先定义函数
	print('Hello, %s.' % name)

Hello = type('Hello', (object,), dict(hello=fn)) # 创建Hello class
h = Hello()
h.hello() #Hello, world.

print type(Hello) #<type 'type'>
print type(h) #<class '__main__.Hello'>

#要创建一个class对象，type()函数依次传入3个参数：

    #1. class的名称；
    #2. 继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
    #3. class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。

print u'-----------------------------2. metaclass------------------------------'
#高阶内容，需要时再掌握