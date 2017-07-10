#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: selectors为多路复用封装庫 默认使用epoll实现多路复用, windows下使用的是select
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: epoll_socket_server.py
# @time: 17/7/10 下午11:42

import selectors
import socket

sel = selectors.DefaultSelector()


def accept(sock, mask):
    conn, addr = sock.accept()  # Should be ready
    print('accepted', conn, 'from', addr)
    conn.setblocking(False)
    sel.register(conn, selectors.EVENT_READ, read)  # 注册监听客户端conn


def read(conn, mask):
    data = conn.recv(1000)  # Should be ready
    if data:
        print('echoing', repr(data), 'to', conn)
        conn.send(data)  # Hope it won't block
    else:
        print('closing', conn)
        sel.unregister(conn)
        conn.close()


server = socket.socket()
server.bind(('localhost', 10000))
server.listen(100)
server.setblocking(False)
sel.register(server, selectors.EVENT_READ, accept)  # 注册监听服务端socket accept为event字典中key中的data

while True:
    events = sel.select()  # 有可能是epoll, 有可能是select, 只要注册的socket有活动 都会返回event然后向下执行
    for key, mask in events:
        callback = key.data  # callback = accept函数/read函数
        callback(key.fileobj, mask)  # key.fileObj = 文件句柄 相当于readable/(server, conn)

if __name__ == '__main__':
    pass
