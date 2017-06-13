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
    cmd_res_size = client.recv(1024)  # 接收命令结果的长度
    cmd_res_size = cmd_res_size.decode('utf-8')
    print('cmd_res_size', cmd_res_size)
    client.send('ack'.encode('utf-8'))
    # 如果大于每次客户端接收的大小 需要循环接收
    received_size = 0
    while received_size < int(cmd_res_size):
        data = client.recv(1024)  # 有可能收到的小于1024 需要用len判断
        received_size += len(data)
        print(data.decode('utf-8'))
    else:
        print('received done')
client.close()
