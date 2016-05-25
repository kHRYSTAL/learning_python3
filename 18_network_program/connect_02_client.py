#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""
@version: ??
@usage: 
@author: kHRYSTAL
@license: Apache Licence 
@contact: khrystal0918@gmail.com
@site: https://github.com/kHRYSTAL
@software: PyCharm
@file: connect_02_client.py
@time: 16/5/25 下午9:30
"""
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
s.connect(('127.0.0.1', 9999))
# 接收欢迎消息:
print(s.recv(1024).decode('utf-8'))
for data in [b'Michael', b'Tracy', b'Sarah']:
    # 发送数据:
    s.send(data)
    print(s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close()


'''
需要注意的是，客户端程序运行完毕就退出了，而服务器程序会永远运行下去，必须按Ctrl+C退出程序。

小结

用TCP协议进行Socket编程在Python中十分简单，对于客户端，要主动连接服务器的IP和指定端口，对于服务器，要首先监听指定端口，然后，对每一个新的连接，创建一个线程或进程来处理。通常，服务器程序会无限运行下去。

同一个端口，被一个Socket绑定了以后，就不能被别的Socket绑定了。
'''


'''
UDP的使用与TCP类似，但是不需要建立连接。
此外，服务器绑定UDP端口和TCP端口互不冲突，也就是说，UDP的9999端口与TCP的9999端口可以各自绑定。
'''


def func():
    pass


class Main():
    def __init__(self):
        pass


if __name__ == '__main__':
    pass