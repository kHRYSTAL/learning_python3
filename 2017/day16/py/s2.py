#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: s2.py
# @time: 17/9/4 下午1:57

from wsgiref.simple_server import make_server
# path指定的函数都在account中
from controler import account

URL_DICT = {
    '/index': account.handle_index,
    '/date': account.handle_date,
}


def RunServer(environ, start_response):
    # environ 客户端发来的数据
    # start_response 封装返回给用户的数据 响应头 状态码
    start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])

    current_path = environ['PATH_INFO']  # 获取请求path
    func = None

    if current_path in URL_DICT:
        func = URL_DICT[current_path]

    if func:
        return func()
    else:
        return ['<h1>404</h1>'.encode('utf-8'), ]

        # 返回的内容
        # return ['<h1>Hello, web</h1>'.encode('utf-8'), ]  # 在py3中 wsgi返回结果为列表 且需要编码


if __name__ == '__main__':
    httpd = make_server('127.0.0.1', 8000, RunServer)
    print('Serving HTTP on port 8000...')
    httpd.serve_forever()
