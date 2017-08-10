#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: http_sample_server.py
# @time: 17/8/11 上午12:08

import socket


def handle_request(conn):
    buf = conn.recv(1024)
    conn.send('HTTP/1.1 200 OK\r\n\r\n'.encode('utf8'))  # 浏览器接受首先需要指明http协议且返回码正确
    conn.send('Hello, Seven'.encode('utf8'))


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', 8000))
    sock.listen(5)  # 最大连接数
    while True:
        conn, addr = sock.accept()
        handle_request(conn)
        conn.close()  # 断开本次连接, 等待accept


if __name__ == '__main__':
    main()
