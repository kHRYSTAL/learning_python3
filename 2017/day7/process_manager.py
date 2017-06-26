#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: Manager, 用于在进程中共享的对象 可以是字典 锁 列表等等
#           Manager 默认是加锁的, 不需要再加锁
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: process_manager.py
# @time: 17/6/26 下午10:25
from multiprocessing import Process, Manager
import os


def f(d, l):
    d[os.getpid()] = os.getpid()
    l.append(os.getpid())
    print(l)


if __name__ == '__main__':
    with Manager() as manager:
        d = manager.dict()  # {}生成一个字典, 可在多个进程间共享和传递
        l = manager.list(range(5))
        p_list = []
        for i in range(10):
            p = Process(target=f, args=(d, l))
            p.start()
            p_list.append(p)

        for res in p_list:
            res.join()  # 主进程需要等待所有进程都执行完, 这样可以看出l中的列表有10个元素

        print(d)
        print(l)
