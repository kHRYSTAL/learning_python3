#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: process_pipes.py
# @time: 17/6/26 上午12:32
from multiprocessing.connection import Pipe

from multiprocessing import Process


def f(conn):
    conn.send(['child send'])
    conn.send(['child send'])
    print(conn.recv())
    conn.close()


if __name__ == '__main__':
    """创建管道 一端给主进程 一端给子进程 用于通讯"""
    parent_conn, child_conn = Pipe()
    p = Process(target=f, args=(child_conn,))
    p.start()

    print(parent_conn.recv())  # 发几次收几次
    print(parent_conn.recv())
    # print(parent_conn.recv())  # 多收会阻塞, 与socket相同
    parent_conn.send('from parent')

