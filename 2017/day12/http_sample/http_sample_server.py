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
    conn.send(bytes('HTTP/1.1 200 OK\r\n\r\n', encoding='utf-8'))  # 浏览器接受首先需要指明http协议且返回码正确
    f = open('index.html', 'r', encoding='utf-8')
    data = f.read()
    f.close()
    import time
    str_time = str(time.time())
    data = data.replace("@@@@@", str_time)  # 替换后需要重新赋值
    conn.send(bytes(data, encoding='utf-8'))


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', 8000))
    sock.listen(5)
    while True:
        conn, addr = sock.accept()
        handle_request(conn)
        conn.close()


if __name__ == '__main__':
    main()
