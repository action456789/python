#!/usr/bin/env python  
# -*- coding: utf-8 -*-

print u'-------------------------客户端------------------------------'

# 编写一个简单的服务器程序，它接收客户端连接，把客户端发过来的字符串加上Hello再发回去。

# 要测试这个服务器程序，我们还需要编写一个客户端程序：

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 建立连接:
s.connect(('127.0.0.1', 9999))

# 接收欢迎消息:
print s.recv(1024)

for data in ['Michael', 'Tracy', 'Sarah']:
    # 发送数据:
    s.send(data)
    print s.recv(1024)

s.send('exit')

s.close()