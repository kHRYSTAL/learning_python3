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
@file: 02_asyncio.py
@time: 16/5/30 上午1:47
"""

'''
asyncio是Python 3.4版本引入的标准库，直接内置了对异步IO的支持。

asyncio的编程模型就是一个消息循环。
我们从asyncio模块中直接获取一个EventLoop的引用，
然后把需要执行的协程扔到EventLoop中执行，就实现了异步IO。
'''

import asyncio


# @asyncio.coroutine
# def hello():
#     print("Hello world!")
#     # 异步调用asyncio.sleep(5)
#     r = yield from asyncio.sleep(1)
#     print("Hello again!")
#
# # 获取EventLoop:
# loop = asyncio.get_event_loop()
# # 执行coroutine
# loop.run_until_complete(hello())
# loop.close()

'''
@asyncio.coroutine把一个generator标记为coroutine类型，
然后，我们就把这个coroutine扔到EventLoop中执行。

hello()会首先打印出Hello world!，
然后，yield from语法可以让我们方便地调用另一个generator。
由于asyncio.sleep()也是一个coroutine，所以线程不会等待asyncio.sleep()，
而是直接中断并执行下一个消息循环。
当asyncio.sleep()返回时，线程就可以从yield from拿到返回值（此处是None），
然后接着执行下一行语句。

'''

'''
#把asyncio.sleep(1)看成是一个耗时1秒的IO操作，
#在此期间，主线程并未等待，而是去执行EventLoop中其他可以执行的coroutine了，因此可以实现并发执行。
'''

#我们用Task封装两个coroutine试试：

import threading
import asyncio


@asyncio.coroutine
def hello1():
    print('Hello1! (%s)' % threading.currentThread())
    yield from asyncio.sleep(1)
    print('Hello1 again! (%s)' % threading.currentThread())


@asyncio.coroutine
def hello2():
    print('Hello2! (%s)' % threading.currentThread())
    yield from asyncio.sleep(1)
    print('Hello2 again! (%s)' % threading.currentThread())

loop = asyncio.get_event_loop()
tasks = [hello1(), hello2()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

# 由打印的当前线程名称可以看出，两个coroutine是由同一个线程并发执行的。

# 如果把asyncio.sleep()换成真正的IO操作，则多个coroutine就可以由一个线程并发执行。

if __name__ == '__main__':
    pass