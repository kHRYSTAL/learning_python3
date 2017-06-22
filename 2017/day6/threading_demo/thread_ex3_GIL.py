#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 使用join函数 使主线程能够接收到所有线程结束的信号
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: thread_ex3_JIL.py
# @time: 17/6/21 下午2:53

import threading
import time

number = 0


def run():
    """
    task
    """
    global number
    time.sleep(2)
    number += 1

t_objs = []
for i in range(1000):
    t = threading.Thread(target=run)
    t_objs.append(t)
    t.start()

for t in t_objs:
    t.join()


print("number:", number)
