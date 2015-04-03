#!/usr/bin/env python  
# -*- coding: utf-8 -*-

print u'-------------------------断言------------------------------'

def foo(s):
	n = int(s)
	assert n != 0, 'n is zero!'
	return 10 / n
#启动Python解释器时可以用-O参数来关闭assert： python -O err.py

print u'-------------------------logging------------------------------'
#logging允许你指定记录信息的级别，有debug，info，warning，error等几个级别，
#当我们指定level=INFO时，logging.debug就不起作用了。同理，指定level=WARNING后，
#debug和info就不起作用了。这样一来，你可以放心地输出不同级别的信息，也不用删除，最后统一控制输出哪个级别的信息。
#logging的另一个好处是通过简单的配置，一条语句可以同时输出到不同的地方，比如console和文件。

import logging
logging.basicConfig(level=logging.INFO)

n = int('0')
logging.info('n = %d' % n)
print 10/n

