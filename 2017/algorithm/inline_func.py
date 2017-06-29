#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: inline_func.py
# @time: 17/6/28 下午7:02


# def f():
#     l = []
#     for i in range(1, 4):
#         def g():
#             print(i)
#             return i * i
#
#         l.append(g)  # list存储的是函数块 三个函数块内存地址不同(因为重新def), 其中包含的i是for循环的i 是同一个引用
#         # 所以i在g里的结果最后都编程了3
#     return l
#
#
# f1, f2, f3 = f()  # [g, g, g]
# print(f1())  # 执行g
# print(f2())
# print(f3())


def count():
    def f(j):
        def g():
            print()
            return j * j

        return g

    l = []
    for i in range(1, 4):
        l.append(f(i))  # 作为参数传递,是对内存的拷贝
    return l


f1, f2, f3 = count()  # [g, g, g]
print(f1())  # 执行g
print(f2())
print(f3())

if __name__ == '__main__':
    pass
