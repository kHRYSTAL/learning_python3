#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 使用协程实现 单线程下多并发的效果(生产者消费者模式)
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: yield_demo.py
# @time: 17/6/26 下午11:55


def producer():
    r = con.__next__()
    r = con2.__next__()
    n = 0
    while n < 5:
        n += 1
        con.send(n)
        con2.send(n)
        print('[producer] is making baozi %s' % n)


def consumer(name):
    print('--->start eating baozi...')
    while True:
        new_baozi = yield
        print('[%s] is eating baozi %s' % (name, new_baozi))


if __name__ == '__main__':
    con = consumer('A')
    con2 = consumer('B')
    producer()
