#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: process_pool.py
# @time: 17/6/26 下午11:25

from multiprocessing import Process, Pool
import time
import os


def Foo(i):
    time.sleep(2)
    print(i + 100)
    return i + 100


def Bar(arg):
    print('-->exec done:', arg, os.getpid())


pool = Pool(processes=5)

for i in range(10):
    pool.apply_async(func=Foo, args=(i,), callback=Bar)  # 并发执行, callback为执行完成回调 执行进程为主进程
    # pool.apply(func=Foo, args=(i,))  # 串行执行

print('end')

pool.close()  # 进程池不再接收新的进程
pool.join()  # 进程池中进程执行完毕后再关闭，如果注释，那么程序直接关闭。
