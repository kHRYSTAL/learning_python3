#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: gevent 模仿io切换, 遇到io就切换 不需要手动写切换代码
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: gevent_demo.py
# @time: 17/6/27 下午10:11

import gevent
import time


def foo():
    print('Running in foo')
    gevent.sleep(2)  # 模拟io A
    print('Explicit 精确的 context switch to foo again')


def bar():
    print('Explicit context to bar')
    gevent.sleep(1)  # 模拟io B
    print('Implicit context switch back to bar')


"""
spawn 发起

按列表顺序遍历执行生成器, 遇到sleep就切换函数, 如果遍历后重新执行, 函数还在sleep, 继续按顺序切换
foo 遇到A 执行bar 遇到B  执行foo A还在执行 切换到foo B执行完了 执行bar后面代码
执行foo

相比串行执行(3秒) 代码执行io就跳转 实际上只执行了2秒
"""
start_time = time.time()
gevent.joinall([
    gevent.spawn(foo),
    gevent.spawn(bar)
])

print(time.time() - start_time)  # 2s左右
