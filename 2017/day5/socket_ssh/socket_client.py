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
# @time: 17/6/9 下午2:51

import socket

client = socket.socket()

client.connect(('localhost', 7777))

while True:
    msg = input('>>:')
    if len(msg) == 0:
        continue
    if msg == 'exit':
        break
    client.send(msg.encode('utf-8'))
    data = client.recv(1024)
    print('client received:', data.decode('utf-8'))

client.close()
