#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: process_lock.py
# @time: 17/6/26 下午10:50
from multiprocessing import Lock, Process


def f(l, n):
    l.acquire()
    print('the num is %d' % n)
    l.release()


if __name__ == '__main__':
    lock = Lock()
    for num in range(100):
        Process(target=f, args=(lock, num)).start()
