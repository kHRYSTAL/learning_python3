#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: socket_server.py
# @time: 17/6/14 下午10:53


import socketserver


class MyHandle(socketserver.BaseRequestHandler):

    def setup(self):
        """父类方法"""
        pass

    def finish(self):
        """父类方法"""
        pass

    """
    服务端处理请求类 所有的请求都会最终都会在handle方法中处理
    每一个请求传递到服务器都会实例化这个类
    需要重写handle
    """

    def handle(self):
        while True:
            try:
                # request实际为conn
                self.data = (self.request.recv(1024)).decode('utf-8').strip()
                # 打印客户端地址
                print('{} wrote:'.format(self.client_address[0]))
                print(self.data)
                if not self.data:
                    break
                # 回复客户端
                self.request.send((self.data).encode('utf-8').upper())
            except ConnectionRefusedError as e:
                print('error:', e)
                break


if __name__ == '__main__':
    HOST, PORT = 'localhost', 9876
    # 创建TCPServer
    server = socketserver.ThreadingTCPServer((HOST, PORT), MyHandle)
    """
    server.handle_request() #只处理一个请求
    server.serve_forever() #处理多个请求，永远执行
    """
    server.serve_forever()
