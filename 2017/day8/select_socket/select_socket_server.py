#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 用python实现多路复用select函数
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: select_socket_server.py
# @time: 17/7/5 下午7:34

"""
select函数 在多路复用中 进程遇到阻塞 向kerenl发送IO处理指令
kernel进行IO处理后向用户进程发送通知 select监听到通知后循环遍历socket找到有结果的socket 将kernel获取到的数据
拷贝到自己的进程中
"""
import select
import socket
import queue

server = socket.socket()
server.bind(('localhost', 9000))
# 允许1000个连接
server.listen(1000)

# 设置为非阻塞
server.setblocking(False)

"""
setblocking 为0 receive 不阻塞 accept不阻塞 直接报错
"""
# server.accept()  # [Errno 35] Resource temporarily unavailable

inputs = [server, ]  # 监测server, 如果server活动了说明有client连接
outputs = []

# read list, write list, exception list  需要内核监测的链接
"""
第一个参数是让内核监测的链接
第二个参数
第三个参数 如果socket链接断了 会放到异常里
返回值 可读的, 可写的, 异常的连接
"""

"""
select 的操作相当于监听一组socket 在没有收到活动的socket通知时是阻塞的
"""
while True:
    readable, writeable, exceptional = select.select(inputs, outputs, inputs)
    print(readable, writeable, exceptional)

    """
    当监听到活动的 会继续执行 获取readable的socket, 建立与客户端的连接
    """
    for r in readable:
        if r is server:  # r是server本身的socket 新来了个连接
            conn, addr = server.accept()
            print(conn, addr)
            # conn.recv(1024) # 由于设置的是不阻塞 且客户端还没发数据 会报错
            # 将conn加到监测列表里 监听客户端与服务端建立的连接是否活动
            inputs.append(conn)
        else:  # r是连接 新来数据
            data = r.recv(1024)
            print('收到数据', data)
            r.send(data)

if __name__ == '__main__':
    pass
