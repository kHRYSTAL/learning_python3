#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 所有的服务器后台实际上都是基于下方代码 接收一个客户端socket, 返回数据后断开
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: s1.py
# @time: 17/9/4 下午1:49

import socket


def handle_request(client):
    buf = client.recv(1024)
    client.send("HTTP/1.1 200 OK\r\n\r\n".encode('utf-8'))
    client.send("Hello Seven".encode('utf-8'))


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', 8000))
    sock.listen(5)
    while True:
        connection, address = sock.accept()
        handle_request(connection)
        connection.close()


if __name__ == '__main__':
    main()
