#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 递归锁 有两层锁
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: recursion_lock.py
# @time: 17/6/21 下午10:40

"""
演示死锁现象 用递归锁解决
外部run3有一层锁
run3 执行run1 有一层锁
run3 执行run2 有一层锁

# run3加锁,执行run1, run1也需要加锁 等待run3释放锁 但run3锁释放需要run3执行完 构成了死锁
这是由于持有通一个锁 因为锁的混乱导致的
为解决这个问题 可改为RLock()
RLock内部使用字典 每个线程函数(run1, run2, run3)(key) 对应不同的锁(value)
"""

import threading


def run1():
    print('grab the first part data')
    lock.acquire()
    global num
    num += 1
    lock.release()
    return num


def run2():
    print('grab the second part data')
    lock.acquire()
    global num2
    num2 += 1
    lock.release()
    return num2


def run3():
    lock.acquire()
    res = run1()
    print('-----between run1 and run2')
    res2 = run2()
    lock.release()
    print(res, res2)


num, num2 = 0, 0
lock = threading.RLock()

print('start')
for i in range(1):
    t = threading.Thread(target=run3)
    t.start()

while threading.active_count() != 1:
    """
    当不是只有主线程存在的情况下输出
    """
    print(threading.active_count())
else:
    print('---- all threads done-----')
    print(num, num2)
