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
@file: server.py
@time: 16/5/29 上午12:08
"""
# 从wsgiref模块导入:
from wsgiref.simple_server import make_server
# 导入我们自己编写的application函数


# 创建一个服务器，IP地址为空，端口是8000，处理函数是application:
from webprogram.hello import application

httpd = make_server('', 8001, application)
print('Serving Http on port 8001...')

#开始监听Http请求
httpd.serve_forever()
#确保以上两个文件在同一个目录下，然后在命令行输入python server.py来启动WSGI服务器：





def func():
    pass


class Main():
    def __init__(self):
        pass


if __name__ == '__main__':
    pass