#!/usr/bin/env python  
# -*- coding: utf-8 -*-

print u'-------------------------单元测试------------------------------'

#测试自定义的类 Dict.py

#为了编写单元测试，我们需要引入Python自带的unittest模块
import unittest
from KSDict import Dict

class TestDict(unittest.TestCase):
	def test_init(self):
		d = Dict(a = 1, b = 'test')
		self.assertEquals(d.a, 1)
		self.assertEquals(d.b, 'test')
		self.assertTrue(isinstance(d, dict))

	def test_key(self):
		d = Dict()
		d['key'] = 'value'
		self.assertEquals(d.key, 'value')

	def test_attr(self):
		d = Dict()
		d.key = 'value'
		self.assertTure('key' in d)
		self.assertEquals(d['key'], 'value')

	def test_keyerror(self):
		d = Dict()
		with self.assertRaises(KeyError): # 通过d['empty']访问不存在的key时，抛出KeyError
			value = d['empty']

	def test_attrerror(self):
		d = Dict()
		with self.assertRaise(AttributeError): # 通过d.empty访问不存在的key时，抛出AttributeError
			value = d.empty

	def setUp(self): # 每调用一个测试方法的前分别被执行。
		print 'setUp...'

	def tearDown(self): # 每调用一个测试方法的后分别被执行。
		print 'tearDown...'

# 1.编写单元测试时，我们需要编写一个测试类，从unittest.TestCase继承。
# 2.以test开头的方法就是测试方法，不以test开头的方法不被认为是测试方法，测试的时候不会被执行。

print u'-------------------------运行单元测试------------------------------'
#在命令行通过 python -m unittest filename.py 直接运行单元测试