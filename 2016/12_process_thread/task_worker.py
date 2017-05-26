#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""
@version: ??
@usage: 
@author: kHRYSTAL
@license: Apache Licence 
@contact: khrystal0918@gmail.com
@site: https://github.com/kHRYSTAL
@software: PyCharm
@file: task_worker.py
@time: 16/5/23 上午11:58
"""

import time, sys, queue
from multiprocessing.managers import BaseManager

class QueueManager(BaseManager):
    pass

#由于这个QueueManager只从网络上获取queue 所以注册时只提供名字

QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

#连接到服务器 即运行task_master.py的机器

server_addr = '127.0.0.1'
print('Connect to server %s...' % server_addr)

#端口验证码与master保持一致

m = QueueManager(address=(server_addr,5000),authkey=b'abc')

m.connect()

task = m.get_task_queue()
result = m.get_result_queue()

# 从task队列取任务,并把结果写入result队列:
for i in range(10):
    try:
        n = task.get(timeout=1)
        print('run task %d * %d...' % (n, n))
        r = '%d * %d = %d' % (n, n, n*n)
        time.sleep(1)
        result.put(r)
    except queue.Queue.Empty:
        print('task queue is empty.')
# 处理结束:
print('worker exit.')

def func():
    pass


class Main():
    def __init__(self):
        pass


if __name__ == '__main__':
    pass