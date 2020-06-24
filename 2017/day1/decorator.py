#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 普通装饰器 和带参数装饰器
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: decorator.py
# @time: 17/5/26 下午7:08
"""
1.函数即变量
2.高阶函数:参数为函数名或返回值为函数名 函数名即函数所在内存的引用
3.嵌套函数 在函数内声明函数
4.函数名+() 即为执行函数
5.高阶函数 + 嵌套函数即为装饰器
"""
import time


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        stop_time = time.time()
        print('cost time: %s' % (stop_time - start_time))

    return wrapper


def timer_args(arg):
    def out_wrapper(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            func(*args, **kwargs)
            stop_time = time.time()
            if arg:
                print('cost time: %s' % (stop_time - start_time))

        return wrapper

    return out_wrapper


@timer
def test1():
    print('in the test1')

"""
@time 相当于
test1 = timer(test1)
所以test1此时为wrapper
"""


@timer_args(True)
def test2(x):
    print('in the test2', x)

test2(111)
"""
带参数相当于
timer_args = timer_args(args)
=> timer_args = out_wrapper
test2 = out_wrapper(test2)
所以此时test2为wrapper
"""


if __name__ == '__main__':
    pass
