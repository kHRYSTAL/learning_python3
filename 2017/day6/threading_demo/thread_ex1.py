#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: thread_ex1.py
# @time: 17/6/20 下午6:21

import threading
import time


def run(n):
    """
    task
    """
    print('task', n)
    time.sleep(2)


# target 参数为执行的目标函数, args 为参数 元组
t1 = threading.Thread(target=run, args=('t1',))
t2 = threading.Thread(target=run, args=('t2',))

t1.start()
t2.start()

run('order1')
run('order2')

