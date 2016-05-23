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
@file: task_master.py
@time: 16/5/23 上午11:58
"""

import random,time, queue
from multiprocessing.managers import BaseManager

#发送任务的队列
task_queen = queue.Queue()

#接收结果的队列
result_queen = queue.Queue()


#从BaseManager继承的QueenManager:
class QueenManager(BaseManager):
    pass

#把两个Queue都注册到网络上,callable参数关联了Queue对象

QueenManager.register('get_task_queue', callable=lambda :task_queen)
QueenManager.register('get_result_queue', callable=lambda :result_queen)

#绑定端口5000,验证码'abc'
manager = QueenManager(address=('', 5000), authkey=b'abc')
#启动Queue:
manager.start()

#获得通过网络访问的Queue对象
task= manager.get_task_queue()
result = manager.get_result_queue()


#放几个任务进去:
for i in range(10):
    n = random.randint(0,10000)
    print('Put task %d...' % n)
    task.put(n)


#从result读取结果
print('Try get results...')

for i in range(10):
    r = result.get(timeout=30)
    print('Result: %s' % r)

#关闭
manager.shutdown()
print('master exit.')
def func():
    pass


class Main():
    def __init__(self):
        pass


if __name__ == '__main__':
    pass