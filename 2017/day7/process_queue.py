#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 用Queue实现进程间通讯
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: process_queue.py
# @time: 17/6/26 上午12:13

from multiprocessing import Queue
from multiprocessing import Process


def f(q):
    q.put([42, None, 'hello'])

if __name__ == '__main__':
    """在子进程中向q设置数据"""
    q = Queue()
    """与线程不同 进程之间的内存是独立的 所以子进程访问不到父进程创建的queue,
     需要把queue作为参数传递给子进程

     [进程之间的共享数据是通过pickle序列化实现的
      说白了就是两个进程操作同一个数据, 数据是一份 但两个进程间的内存对象是两份]
      需要注意两个进程同时修改同一份数据的问题
     """
    p = Process(target=f, args=(q,))
    p.start()
    """在主进程获取数据"""
    print(q.get())
