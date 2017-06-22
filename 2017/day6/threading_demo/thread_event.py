#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: thread_event.py
# @time: 17/6/22 下午12:00
import time
import threading

event = threading.Event()


def lighter():
    count = 0
    event.set()
    while True:
        if count > 5 and count <10:  # 改成红灯停, 清空后 车辆线程会wait()
            event.clear()  # 清空标志位
            print('\033[41;1m红灯停\033[0m')
        elif count > 10:  # 改成绿灯行, 设置标志位 车辆线程会执行wait()后的代码
            event.set()  # 设置标志位, count归零
            count = 0
        else:  # 小于5
            print('\033[42;1m绿灯行\033[0m')
        time.sleep(1)
        count += 1


def car(name):
    while True:
        if event.is_set():  # 代表绿灯
            print('[%s is run]' % name)
            time.sleep(1)
        else:
            print('[%s sees red light, waiting...]' % name)
            event.wait()  # 阻塞, 等待event被set
            print('[%s] green light is on start going' % name)


light = threading.Thread(target=lighter)
light.start()
car1 = threading.Thread(target=car, args=('tesla',))
car1.start()
