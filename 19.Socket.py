#!/usr/bin/env python  
# -*- coding: utf-8 -*-

print u'-------------------------网络编程------------------------------'

print u'-------------------------1. 连接新浪------------------------------'

#创建一个基于TCP连接的Socket
import socket

# 1. 创建socket对象:

# AF_INET 指定使用IPv4协议，如果要用IPv6，指定为AF_INET6

# SOCK_STREAM 指定使用面向流的TCP协议
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. 建立连接
# 以连接到新浪服务器为例，端口需指定为80，因为端口是Web服务的标准端口
s.connect(('www.sina.com.cn', 80))

# 3. 发送数据
# 建立TCP连接后，我们就可以向新浪服务器发送请求，要求返回首页的内容

# TCP连接创建的是双向通道，双方都可以同时给对方发数据。但是谁先发谁后发，怎么协调，要根据具体的协议来决定。

# 例如，HTTP协议规定客户端必须先发请求给服务器，服务器收到后才发数据给客户端。

# 发送的文本格式必须符合HTTP标准，如果格式没问题，接下来就可以接收新浪服务器返回的数据了：
s.send('GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

# 4. 接收数据

# 接收数据时，调用recv(max)方法，一次最多接收指定的字节数，

# 因此，在一个while循环中反复接收，直到recv()返回空数据，表示接收完毕，退出循环。
buffer = []
while True:
	# 每次最多接收1K字节
	 d = s.recv(1024)
	 if d:
	 	buffer.append(d)
	 else:
	 	break

data = ''.join(buffer)

# 5.关闭Socket

# 当我们接收完数据后，调用close()方法关闭Socket，这样，一次完整的网络通信就结束了：
s.close()

# 接收到的数据包括HTTP头和网页本身，我们只需要把HTTP头和网页分离一下，把HTTP头打印出来，网页内容保存到文件：
header, html = data.split('\r\n\r\n', 1)
print header
# 把接收的数据写入文件:
with open ('./testdir/sina.html', 'wb') as f:
	f.write(html)

print u'------------------------- 2. 服务器端 ------------------------------'

# 见 Server.py

print u'------------------------- 3. 客户端 ------------------------------'

# 见 Client.py