#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 可设置优先级的队列 数字越小优先级越高
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: queue_vip.py
# @time: 17/6/22 下午5:33
import queue

q = queue.PriorityQueue()


q.put((-1, 'ich'))
q.put((6, 'ddd'))
q.put((-3, 'tom'))
q.put((10, 'khrystal'))

print(q.get())
print(q.get())
print(q.get())
print(q.get())
