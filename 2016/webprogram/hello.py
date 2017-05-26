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
@file: hello.py.py
@time: 16/5/29 上午12:05
"""
'''
environ：一个包含所有HTTP请求信息的dict对象；接收request中包含的数据
start_response：一个发送HTTP响应的函数。
'''


def application(environ, start_response):
    #服务器响应的header
    start_response('200 OK', [('Content-Type', 'text/html')])
    #服务器响应的body
    #return [b'<h1>Hello, web!</h1>']
    body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')
    print(body.encode('utf-8'))
    return [body.encode('utf-8')]


def func():
    pass


class Main():
    def __init__(self):
        pass


if __name__ == '__main__':
    pass