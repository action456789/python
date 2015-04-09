#!/usr/bin/env python  
# -*- coding: utf-8 -*-
print u'-------------------------常用内建模块------------------------------'


print u'-------------------------1. collections------------------------------'
print u'-------------------------1.1 namedtuple------------------------------'
# namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数。
# 我们用 namedtuple 定义一种数据类型，它具备tuple的不变性，又可以根据属性来引用。
from collections import namedtuple

# 定义一个点
# namedtuple('名称', [属性list]):
point = namedtuple('point', ['x', 'y'])
p = point(1, 2)
print p.x, p.y
print isinstance(p, point)
print isinstance(p, tuple)

# 定义一个圆
circle = namedtuple('circle', ['x', 'y', 'r'])

print u'-------------------------1.2 deque------------------------------'
#使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，因为list是线性存储，数据量大的时候，插入和删除效率很低。
#deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈
from collections import deque

q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print q

print u'-------------------------1.3 defaultdict------------------------------'

#使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict：
from collections import defaultdict

dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print dd['key1']
print dd['key2'] # key2不存在，返回默认值

print u'-------------------------1.4 OrderedDict------------------------------'
#使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。
#如果要保持Key的顺序，可以用OrderedDict：
from collections import OrderedDict

d = dict([('a', 1), ('b', 2), ('c', 3)])
print d # dict的Key是无序的

od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print od  # OrderedDict的Key是有序的

print u'-------------------------1.5 Counter------------------------------'
# Counter是一个简单的计数器，例如，统计字符出现的个数：
from collections import Counter

c = Counter()
for ch in 'programming':
	c[ch] = c[ch] + 1

print c #Counter({'g': 2, 'm': 2, 'r': 2, 'a': 1, 'i': 1, 'o': 1, 'n': 1, 'p': 1})

print u'-------------------------2 base64------------------------------'
# Base64是一种用64个字符来表示任意二进制数据的方法。
# Base64是一种通过查表的编码方法，不能用于加密
# Base64适用于小段内容的编码，比如数字证书签名、Cookie的内容等
import base64

print base64.b64encode('binary\x00string') #YmluYXJ5AHN0cmluZw==
print base64.b64decode('YmluYXJ5AHN0cmluZw==')

print u'-------------------------2.1 url safe base64------------------------------'
#由于标准的Base64编码后可能出现字符+和/，在URL中就不能直接作为参数，
#所以又有一种"url safe"的base64编码，其实就是把字符+和/分别变成-和_：
print base64.b64encode('i\xb7\x1d\xfb\xef\xff') # abcd++//
print base64.urlsafe_b64encode('i\xb7\x1d\xfb\xef\xff') # abcd--__
print base64.urlsafe_b64decode('abcd--__')

print u'-------------------------2.2 等号的处理------------------------------'
# 由于=字符也可能出现在Base64编码中，但=用在URL、Cookie里面会造成歧义，所以，很多Base64编码后会把=去掉：
print base64.b64decode('YWJjZA==') # abcd
#print base64.b64decode('YWJjZA') #TypeError: Incorrect padding

#去掉=后怎么解码呢？因为Base64是把3个字节变为4个字节，所以，Base64编码的长度永远是4的倍数，
#因此，需要加上=把Base64字符串的长度变为4的倍数，就可以正常解码了。
#请写一个能处理去掉=的base64解码函数：
def safe_b64decode(b):
	i = len(b) % 4
	if i == 0:
		return base64.b64decode(b)
	else:
		while i < 4:
			b += '='
			i = i + 1
		return base64.b64decode(b)
	
print safe_b64decode('YWJjZA')

print u'-------------------------3 hashlib------------------------------'
#Python的hashlib提供了常见的摘要算法，如MD5，SHA1等等。
print u'-------------------------3.1 md5------------------------------'
#MD5是最常见的摘要算法，速度很快，生成结果是固定的128 bit字节，通常用一个32位的16进制字符串表示。
import hashlib

md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?')
print md5.hexdigest()

#如果数据量很大，可以分块多次调用update()，最后计算的结果是一样的：
md5 = hashlib.md5()
md5.update('how to use md5 ')
md5.update('in python hashlib?')
print md5.hexdigest()

print u'-------------------------3.2 SHA1------------------------------'
#SHA1的结果是160 bit字节，通常用一个40位的16进制字符串表示。
#比SHA1更安全的算法是 SHA256 和 SHA512，不过越安全的算法越慢，而且摘要长度更长。

sha1 = hashlib.sha1()
sha1.update('how to use md5 ')
sha1.update('in python hashlib?')
print sha1.hexdigest()

print u'-------------------------3.3 模拟用户注册，计算更安全的MD5------------------------------'
#根据用户输入的登录名和口令模拟用户注册，计算更安全的MD5：
import hashlib

db = {}
the_salt = 'ke action' #加盐 

def get_md5(s):
	md5 = hashlib.md5()
	md5.update(s)
	return md5.hexdigest() 

def register(username, password):
	db[username] = get_md5(username + password + the_salt)

register('ks', '111111')
print db

print u'-------------------------4 itertools------------------------------'
#Python的内建模块itertools提供了非常有用的用于操作迭代对象的函数。

#无限序列只有在for迭代时才会无限地迭代下去，如果只是创建了一个迭代对象，
#它不会事先把无限个元素生成出来，事实上也不可能在内存中创建无限多个元素。

#首先，我们看看itertools提供的几个“无限”迭代器：
import itertools

print u'-------------------------4.1 count()------------------------------'
# count(i)会创建一个从i开始累加的无限的迭代器

#打印所有自然数
for n in itertools.count(2):
	print n 
	
	if(n > 9):
		break

print u'-------------------------4.2 cycle()------------------------------'
#cycle()会把传入的一个序列无限重复下去：
i = 0
for c in itertools.cycle('ABC'):
	print c
	
	i += 1
	if (i > 10):
		break

print u'-------------------------4.3 repeat()------------------------------'
#repeat()负责把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数：

for n in itertools.repeat('ABC', 10):
	print n

print u'-------------------------4.4 takewhile()------------------------------'
#无限序列可以无限迭代下去，我们可以通过takewhile()等函数根据条件判断来截取出一个有限的序列：

for n in itertools.takewhile(lambda x: x < 10, itertools.count(1)):
	print n

print u'-------------------------4.5 chain()------------------------------'
#chain()可以把一组迭代对象串联起来，形成一个更大的迭代器

for c in itertools.chain('ABC', 'abc'):
	print c

print u'-------------------------4.6 groupby()------------------------------'
#groupby()把迭代器中相邻的重复元素挑出来放在一起：

for key, group in itertools.groupby('AAABBBCCDAA'):
	print key, list(group)

print '\n'
#实际上挑选规则是通过函数完成的，只要作用于函数的两个元素返回的值相等，这两个元素就被认为是在一组的，
#而函数返回值作为组的key。如果我们要忽略大小写分组，就可以让元素'A'和'a'都返回相同的key：
for key, group in itertools.groupby('AaabBBcCdaa', lambda c: c.upper()):
	print key, list(group)

print u'-------------------------4.7 imap()------------------------------'
#imap()和map()的区别在于，imap()可以作用于无穷序列，并且，如果两个序列的长度不一致，以短的那个为准。

#取两个序列中的元素进行 lambda 运算
for x in itertools.imap(lambda x, y: x*y, [10, 20, 30], itertools.count(2)):
	print x

#注意imap()返回一个迭代对象，而map()返回list。当你调用map()时，已经计算完毕
#当你调用imap()时，并没有进行任何计算：
print map(lambda x: x*x, [1, 2, 3])
print itertools.imap(lambda x: x*x, [1, 2, 3])

#必须用for循环对r进行迭代，才会在每次循环过程中计算出下一个元素.
#这说明imap()实现了“惰性计算”，也就是在需要获得结果的时候才计算。类似imap()这样能够实现惰性计算的函数就可以处理无限序列：
r = itertools.imap(lambda x: x*x, itertools.count(1))
for n in itertools.takewhile(lambda x: x < 20, r):
	print n


print '\n'
#使用map处理无限序列会出现错误：
r = map(lambda x: x*x, itertools.count(1))
for n in map(lambda x: x*x, itertools.count(1)): #MemoryError
	print n 

print u'-------------------------4.8 ifilter()------------------------------'
#不用多说了，ifilter()就是filter()的惰性实现。