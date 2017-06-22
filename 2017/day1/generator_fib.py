#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 生成器
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: generator_fib.py
# @time: 17/5/26 下午7:14
"""
1.next就开始执行到yield处中断 并抛出yield右侧的值
2.yield 就中断
"""


def fib(max):
    """斐波那契函数"""
    n, a, b = 0, 0, 1
    while n < max:
        n += 1
        yield b
        a, b = b, a + b
    return 'done'  # 当next不会再执行时 会执行到这里 抛出StopIteration异常


f = fib(10)

f.__next__()
next(f)

for i in f:  # 生成器可以被for循环迭代 是迭代器 这里的for循环实际上是不断调用next()
    print(i)

"""
a, b = b, a+b
相当于:
temp = tuple(a, a+b)
a = temp[0]
b = temp[1]
"""
if __name__ == '__main__':
    pass
