#!/usr/bin/env python     
#-*- coding: utf-8 -*-   

#文件开头第一句表示：让这个文件可以直接在Unix/Linux/Mac上运行 
#文件开头第二句表示：让.py文件使用标准UTF-8编码

'A Test Module'
#表示模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释；

__author__ = 'kesen'

print u'------------------------1. 使用模块-----------------------------'

import sys  #导入模块

def test():
	args = sys.argv  #变量sys指向导入的sys模块

	# sys模块有一个argv变量，用list存储了命令行的所有参数。argv至少有一个元素，因为第一个参数永远是该.py文件的名称
	# 运行python hello.py获得的sys.argv就是['hello.py']
	# 运行python hello.py Michael获得的sys.argv就是['hello.py', 'Michael]。
	if len(args) == 1:
		print  'Hello World!'
	elif len(args) == 2:
		print 'Hello, %s' %args[1]
	else:
		print 'Too many arguments!'

if __name__ == '__main__': 
	#命令行模式下才会运行下面的代码
	test()
	print sys.argv[0]

print u'------------------------2. 别名-----------------------------'
	
#导入模块时，还可以使用别名，这样，可以在运行时根据当前环境选择最合适的模块。
#比如Python标准库一般会提供StringIO和cStringIO两个库，这两个库的接口和功能是一样的，
#但是cStringIO是C写的，速度更快，所以，你会经常看到这样的写法：

try:
	import cStringIO as StringIO
except importError:  # 导入失败会捕获到ImportError
	import StringIO

#这样就可以优先导入cStringIO。如果有些平台不提供cStringIO，还可以降级使用StringIO。
#导入cStringIO时，用import ... as ...指定了别名StringIO，因此，后续代码引用StringIO即可正常工作。

#还有类似simplejson这样的库，在Python 2.6之前是独立的第三方库，从2.6开始内置，所以，会有这样的写法：
try:
    import json # python >= 2.6
except ImportError:
    import simplejson as json # python <= 2.5

print u'------------------------3. 导入自定义模块-----------------------------'

from hello import Hello #导入hello模块的Hello
h = Hello()
h.hello()