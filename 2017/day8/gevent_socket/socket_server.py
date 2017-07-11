#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 使用协程实现socket并发
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: socket_server.py
# @time: 17/6/27 下午11:25


import sys
import socket
import time
import gevent

from gevent import socket, monkey

monkey.patch_all()

"""
打了mokey补丁后 这个程序的所有阻塞都会切换函数
本身server是单线程阻塞的 如果client连接后不close
handle_request只能处理单个连接的消息, 且handle_request不处理完 无法接收新的client发送的消息和建立通道
将handle加入协程后 遇到阻塞, 由于打了monkey, 会回到s.accept进行监听新的client连接 这样就能接收到新的client连接消息 建立通道
如:client1发送消息 server可以接收到并处理, client2发送消息 server可以接收到并处理
实际上gevent 这时候维护了两个handle_request函数 每个handle_request函数有不同的conn对象
"""


def server(port):
    s = socket.socket()
    s.bind(('0.0.0.0', port))
    s.listen(500)
    while True:
        print('before accept')
        cli, addr = s.accept()  # io阻塞
        print('new connection')
        gevent.spawn(handle_request, cli)  # 将conn加入协程


def handle_request(conn):
    try:
        while True:
            data = conn.recv(1024)  # io阻塞
            print("recv:", data)
            conn.send(data)
            if not data:
                conn.shutdown(socket.SHUT_WR)

    except Exception as  ex:
        print(ex)
    finally:
        conn.close()


if __name__ == '__main__':
    server(8001)
