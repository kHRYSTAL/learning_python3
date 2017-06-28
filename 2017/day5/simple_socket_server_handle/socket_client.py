#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: socket_client.py
# @time: 17/6/14 下午11:04


import socket

# 声明socket类型 同时生成socket连接对象
client = socket.socket()

client.connect(('localhost', 9876))
while True:
    msg = input('>>:')
    if len(msg) == 0:  # 服务端和客户端不能发送和接收空如果为空,跳出本次循环
        continue
    client.send(msg.encode('utf-8'))
    # 阻塞状态 等待接收
    data = client.recv(1024)
    print('client receive:', data.decode('utf-8'))

client.close()