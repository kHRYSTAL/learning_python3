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
@file: 03_async_await.py
@time: 16/5/30 下午9:37
"""

'''
用asyncio提供的@asyncio.coroutine可以把一个generator标记为coroutine类型，然后在coroutine内部用yield from调用另一个coroutine实现异步操作。

为了简化并更好地标识异步IO，从Python 3.5开始引入了新的语法async和await，可以让coroutine的代码更简洁易读。

请注意，async和await是针对coroutine的新语法，要使用新的语法，只需要做两步简单的替换：

把@asyncio.coroutine替换为async；
把yield from替换为await。
让我们对比一下上一节的代码：
'''

import asyncio

@asyncio.coroutine
def hello1():
    print("Hello world")
    r = yield from asyncio.sleep(1)
    print("Hello again")


async def hello2():
    print("Hello, world")
    r = await asyncio.sleep(1)
    print("Hello again")


loop = asyncio.get_event_loop()
tasks = [hello1(), hello2()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

if __name__ == '__main__':
    pass

