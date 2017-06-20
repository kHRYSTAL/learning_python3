#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: thread_ex2.py
# @time: 17/6/20 下午6:28


import threading
import time


class MyThread(threading.Thread):
    def __init__(self, num):
        """ 因为重写了父类的方法 需要调用父类的方法 """
        super(MyThread, self).__init__()
        self.num = num

    def run(self):
        """
        定义每个线程需要运行的函数 该函数为父类实现的空方法
        """
        print('running task', self.num)
        time.sleep(2)
        print('done--- %s' % self.num)


t1 = MyThread('t1')
t2 = MyThread('t2')
#
# t1.start()
# t1.join()  # = wait() 将线程加入到当前脚本主线程 相当于串行 t1不执行完 t2不会执行start()
# # 如果将t2.start()放到join()之上 可以通过join()函数控制线程执行完成之后才能继续向下执行
# t2.start()

start_time = time.time()
t_objs = []  # 将数据添加到列表里,用于循环执行完执行join()
for i in range(20):
    t = MyThread(('i=%s' % i))
    t.setDaemon(True) # 一定要在start之前设置
    t.start()
    t_objs.append(t)

# for t in t_objs:
#     t.join()
print('cost time:', time.time() - start_time)
# 当前线程
print('main thread:', threading.current_thread())
# 活动线程个数
print(threading.active_count())
