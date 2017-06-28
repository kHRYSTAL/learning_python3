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
import gevent
from gevent import monkey

monkey.patch_all()  # 将socket打热补丁 替换成了gevent中的socket, 遇到recv send accept 就会switch到其他生成器


def handle_request(conn):
    while True:
        data = conn.recv(1024)
        if not data:
            print('client is lost')
            break
        print(type(data))
        print('server receive:', data.decode(encoding='utf-8'))
        conn.send(data)


# 单个server 实现多连接
server = socket.socket()
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# 绑定地址和端口
server.bind(('localhost', 6869))
# 监听
server.listen()
# 等待客户端消息
print('start server success')

while True:
    # 此处可以理解成阻塞, 等待消息
    # 实际上也是非阻塞的
    conn, addr = server.accept()  # 第一次while循环 没有其他生成器 卡在switch
    """
    由于下方函数加入了gevent 则是协程式函数, 相当于g = generator, next(g) 则继续while循环
    server继续等待accept(), 每新来一个连接 都会新增一个生成器

    使用monkey使单线程上接收消息不阻塞, 即 遇到阻塞就switch到其他生成器
    可以理解成, 如果有两个连接, 就有两个handle_request生成器
    在遇到阻塞时 两个生成器内部频繁在阻塞位置切换, 等待其中一个生成器不阻塞时 继续向下执行
    遇到阻塞 再挂起频繁切换
    """
    gevent.spawn(handle_request, conn)




# server.close()
