#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 生成器 生产者消费者问题
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: generator_consumer_producer.py
# @time: 17/5/26 下午7:27

"""
通过生成器实现生产者消费者问题
因为生成器可以在函数中中断 并在中断出恢复
通过send(arg) 可以在中断位置处传值
例子代码是单线程的 但是能够实现类似的并发效果 (协程 函数运行时中断并切换)
"""


def consumer(name):
    print('prepare start: %s' % name)
    while True:
        y = yield  # 接受send的传值并执行next
        print('%s has consumed %s' % (name, y))


def producer():
    a = consumer('A')
    b = consumer('B')
    next(a)
    next(b)
    for i in range(10):
        a.send(i)
        b.send(i)

producer()


if __name__ == '__main__':
    pass
