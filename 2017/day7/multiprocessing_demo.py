#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 通过多进程实现同一时间有两个线程执行
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: multiprocessing_demo.py
# @time: 17/6/23 下午2:05
import multiprocessing
import threading
import time


def thread_run():
    print(threading.get_ident())


def f(name, num):
    time.sleep(2)
    print('hello ', name, num)
    # 在进程中启动线程
    t = threading.Thread(target=thread_run)
    t.start()


if __name__ == '__main__':
    for i in range(10):
        p = multiprocessing.Process(target=f, args=('bob', i))
        p.start()
        # p.join()
