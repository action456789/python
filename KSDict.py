#!/usr/bin/env python  
# -*- coding: utf-8 -*-

#定义一个字典类，使其能通过点语法来访问，如：

class Dict(dict):
	"""docstring for Dict"""
	def __init__(self, **kw):
		super(Dict, self).__init__(**kw)

	def __getattr__(self, key):
		try:
			return self[key]
		except KeyError:
			raise AttributeError(r"'Dict' objct has no attribute '%s'" % key)

	def __setattr__(self, key, value):
		self[key] = value