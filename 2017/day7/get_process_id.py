#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: get_process_id.py
# @time: 17/6/25 下午11:37

import os

from multiprocessing import Process


def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process id', os.getppid())
    print('process id:', os.getpid())
    print('\n\n')


def f(name):
    info('\033[31;1mfunction f\033[0m')
    print('hello', name)


if __name__ == '__main__':
    """ 父进程为terminal id, 当前程序进程id """
    info('\033[32;1mmain process line\033[0m')
    """ 父进程为当前程序进程id, 子进程为新建的进程id"""
    p = Process(target=f, args=('bob',))
    p.start()