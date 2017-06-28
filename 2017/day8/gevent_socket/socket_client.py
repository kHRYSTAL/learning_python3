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
# @time: 17/6/27 下午11:36


import socket

HOST = 'localhost'    # The remote host
PORT = 8001           # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
while True:
    msg = bytes(input(">>:"), encoding="utf8")
    s.sendall(msg)
    data = s.recv(1024)
    #print(data)

    print('Received', repr(data))
s.close()