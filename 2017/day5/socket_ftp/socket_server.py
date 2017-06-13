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
# @time: 17/6/13 下午4:42
import hashlib
import socket, os, time

server = socket.socket()
server.bind(('0.0.0.0', 9999))

server.listen()

while True:
    conn, addr = server.accept()
    print('new connection', addr)
    while True:
        data = conn.recv(1024)
        if not data:
            print('disconnect client')
            break
        cmd, filename = data.decode().split()
        print(filename)
        if os.path.isfile(filename):
            print('isfile')
            f = open(filename, 'rb')
            m = hashlib.md5()
            file_size = os.stat(filename).st_size  # 获取文件大小
            print('filesize:', file_size)
            conn.send(str(file_size).encode())  # send file size
            conn.recv(1024)  # wait for ack
            for line in f:
                m.update(line)
                conn.send(line)
            print('file md5', m.hexdigest())
            f.close()
        print('send done')

server.close()
