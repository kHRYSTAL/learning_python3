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
# @time: 17/6/13 下午4:42

import socket
import hashlib

client = socket.socket()
client.connect(('localhost', 9999))
while True:
    cmd = input('>>:').strip()
    if len(cmd) == 0:
        continue
    if cmd == 'exit':
        break
    if cmd.startswith('get'):  # 获取文件
        client.send(cmd.encode('utf-8'))
        server_response = client.recv(1024)
        print('server response:', server_response.decode('utf-8'))
        client.send(b'ready to receive file')  # 向服务端发送确认请求
        file_total_size = int(server_response.decode('utf-8'))
        received_size = 0
        filename = cmd.split()[1]
        f = open(filename + '.new', 'wb')
        m = hashlib.md5()
        while received_size < file_total_size:
            data = client.recv(1024)
            received_size += len(data)
            m.update(data)
            f.write(data)
            print(file_total_size, received_size)
        else:
            client.send(b'received done')  # 发送完成消息
            new_file_md5 = m.hexdigest()
            print('file received done', received_size, file_total_size)
            f.close()

        server_file_md5 = client.recv(1024)
        print("server file md5:", server_file_md5.decode('utf-8'))
        print("client file md5:", new_file_md5)

client.close()
