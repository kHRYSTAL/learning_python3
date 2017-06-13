#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: socket_server.py
# @time: 17/6/9 下午2:54

import socket
import os

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 7777))
server.listen()
while True:
    conn, addr = server.accept()
    while True:
        data = conn.recv(1024)
        if not data:
            print('client is lost')
            break
        res = os.popen(data.decode('utf-8')).read()

        if len(res) == 0:
            res = 'cmd has no output'

        conn.send(str(len(res.encode('utf-8'))).encode('utf-8'))  # 先发数据大小给客户端
        print('send len ', str(len(res)).encode('utf-8'))
        client_ack = conn.recv(1024)  # wait client to confirm
        conn.send(res.encode('utf-8'))  # 连续send有可能导致粘包, 因此在中间插入一条确认接收的方法
        print('send res', res)

server.close()
