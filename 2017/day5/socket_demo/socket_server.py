#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: server端
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: socket_server.py
# @time: 17/6/9 上午11:39

import socket

server = socket.socket()

# 绑定地址和端口
server.bind(('localhost', 6869))
# 监听
server.listen()
# 等待客户端消息
print('start server success')
# 此处阻塞 等待消息
while True:
    conn, addr = server.accept()
    """
    <socket.socket fd=6, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 6869), raddr=('127.0.0.1', 57030)> ('127.0.0.1', 57030)
    """
    print(conn, addr)
    while True:
        data = conn.recv(1024)
        if not data:
            print('client is lost')
            break
        print(type(data))
        print('server receive:', data.decode(encoding='utf-8'))
        conn.send(data)

# server.close()


