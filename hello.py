#!/usr/bin/env python  
# -*- coding: utf-8 -*-
import os

class Hello(object):
	def hello(self, name = 'world'):
		print ('hello, %s.' % name)

# 返回./testdir/filename
def dataPathHere(filename): 
	datapath = os.path.join(os.path.abspath('.'), 'testdir') # ./testdir
	filePath = os.path.join(datapath, filename) # ./testdir/filename
	return filePath
