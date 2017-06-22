#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: semaphore.py
# @time: 17/6/21 下午11:10


import threading
import time
"""
信号量相当于n把锁
如果线程持有锁达到了最大值n 没有持有锁的线程只能等待
"""


def run(n):
    semaphore.acquire()
    time.sleep(1)
    print('run the thread %s' % n)
    semaphore.release()


if __name__ == '__main__':
    semaphore = threading.BoundedSemaphore(5)  # 最多允许5个线程同时执行
    for i in range(20):
        t = threading.Thread(target=run, args=(i,))
        t.start()

    while threading.active_count() != 1:
        """
        当不是只有主线程存在的情况下输出
        """
        pass
    else:
        print('done')
