#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: queue_ex1.py
# @time: 17/6/22 下午4:43
import queue

# 实例化先进先出队列
q = queue.Queue()

q.put('d1')
q.put('d2')
q.put('d3')

print(q.qsize())

print(q.get())  # 获取d1
print(q.get())  # 获取d2
print(q.get())  # 获取d3

"""
再调用q.get() 由于没有数据 会阻塞
可以调用q.get_nowait()
如果没有数据会抛出异常
或者判断q.qsize()
"""
try:
    q.get_nowait()
except Exception as e:
    print('Empty')

"""
参数block 为True就是没数据时阻塞, time 为超时时间
Queue.get(block=True, timeout=None)
"""
# 可以设置队列最大容量
# q = queue.Queue(maxsize=3)
# 如果队列满了 再put会阻塞

