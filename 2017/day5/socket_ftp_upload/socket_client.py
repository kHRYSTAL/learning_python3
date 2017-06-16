#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: socket_client.py
# @time: 17/6/16 上午10:04

import socket
import os
import json


# client = socket.socket()


class FtpClient(object):
    def __init__(self):
        self.client = socket.socket()

    def help(self):
        msg = '''
        ls
        pwd
        cd ../..
        get filename
        put filename
        '''

    def connect(self, ip, port):
        self.client.connect((ip, port))

    def interactive(self):
        # self.authenticate()
        while True:
            cmd = input('>>').strip()
            if len(cmd):
                continue
            cmd_str = cmd.split()[0]
            if hasattr(self, 'cmd_%s' % cmd_str):
                func = getattr(self, 'cmd_%s' % cmd_str)
                func(cmd)

    def cmd_put(self, *args):
        cmd_split = args[0].split()
        if len(cmd_split) > 1:
            filename = cmd_split[1]
            if os.path.isfile(filename):
                filesize = os.stat(filename).st_size
                msg_dic = {
                    'action': 'put',
                    'filename': filename,
                    'size': filesize,
                    'overridden': True,
                }
                self.client.send(json.dump(msg_dic).encode('utf-8'))
                print('send', json.dumps(msg_dic).encode('utf-8'))
                # 防止粘包 等待服务器确认
                server_response = self.client.recv(1024)
                f = open(filename, 'rb')
                for line in f:
                    self.client.send(line)
                else:
                    print('file upload success...')
                    f.close()
            else:
                print(filename, 'is not exist')

    def cmd_get(self):
        pass


ftp = FtpClient()
ftp.connect('localhost', 9999)
ftp.interactive()
