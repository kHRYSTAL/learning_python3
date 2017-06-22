#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 后进先出
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: queqe_lifo.py
# @time: 17/6/22 下午4:54
import queue

q = queue.LifoQueue()

q.put(1)
q.put(2)
q.put(3)

print(q.get())
print(q.get())
print(q.get())

try:
    q.get_nowait()
except Exception as e:
    print('Empty')
