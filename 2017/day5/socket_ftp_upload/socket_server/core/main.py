#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: main.py
# @time: 17/6/16 上午11:50

import socketserver
import json
import os


class MyTCPHandler(socketserver.BaseRequestHandler):
    def put(self, *args):
        """接收客户端上传的文件"""
        cmd_dic = args[0]
        filename = cmd_dic['filename']
        filesize = cmd_dic['size']
        if os.path.isfile(filename):
            f = open(filename + '.new', 'wb')
        else:
            f = open(filename, 'wb')
        self.request.send(b'200 OK')
        received_size = 0
        while received_size < filesize:
            data = self.request.recv(1024)
            f.write(data)
            received_size += len(data)
        else:
            print('file [%s] has uploaded...' % filename)

    def handle(self):
        while True:
            try:
                self.data = self.request.recv(1024).strip()
                print('{} wrote:'.format(self.client_address[0]))
                cmd_dic = json.load(self.data.decode())
                action = cmd_dic['action']
                if hasattr(self, action):
                    func = getattr(self, action)
                    func(cmd_dic)
                pass
            except ConnectionRefusedError as e:
                print('error:', e)
                break


if __name__ == '__main__':
    HOST, PORT = 'localhost', 9999
    # Create the server, binding to localhost on port 9999
    server = socketserver.ThreadingTCPServer((HOST, PORT), MyTCPHandler)
    server.serve_forever()
