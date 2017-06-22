#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 通过线程 队列实现生产者消费者模型
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: produce_consume.py
# @time: 17/6/22 下午6:19

import threading
import time
import queue

q = queue.Queue(10)


def producer(name):
    count = 1
    while True:
        print('生产骨头%s' % count)
        q.put('骨头%s' % count)
        time.sleep(1)
        count += 1


def consumer(name):
    while True:
        print('[%s] 取到 [%s]' % (name, q.get()))
        time.sleep(1)


p = threading.Thread(target=producer, args=('kHRYSTAL',))
c = threading.Thread(target=consumer, args=('Baladuu',))
c1 = threading.Thread(target=consumer, args=('Dingding',))

p.start()
c.start()
c1.start()
