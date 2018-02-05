#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 幸运数字问题
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: lucky_number.py
# @time: 18/2/6 上午12:17
"""
幸运数字问题.
只有4或7组成的数字为幸运数字
如, 4, 7, 44, 47, 77...
请输入第n位数字 求出第n位的幸运数字是多少
序号      幸运数字    模拟二进制   规律
0         -          -          2^1 - 2
1         4          0
2         7          1          2^2 - 2
3         44         00
4         47         01         2^2 - 2 + 2^1
5         74         10
6         77         11         2^3 - 2
7         444        000
8         447        001
9         474        010
10        477        011        2^3 - 2 + 2 ^ 2
11        744        100
12        747        101
13        774        110
14        777        111        2^4 - 2

可见:
1. n对应的幸运数字的长度为 n <= 2^(length + 1) - 2
"""


def get_lucky_number(n):
    if n == 0:
        return
    import math
    length = -1
    # 获取这个幸运数字的长度
    i = 2
    while True:
        if n <= math.pow(2, i) - 2:
            length = i - 1
            break
        else:
            i += 1
    # 根据mid获取幸运数字
    str = ''
    while length > 0:
        # print(n, length)
        if n > math.pow(2, length) - 2 + math.pow(2, length - 1):
            str += '7'
            # 二进制数左移 如 13 为 774 变为 74 需要减 2 ^ length
            n -= math.pow(2, length)
        else:
            str += '4'
            # 二进制数左移 如 9 为 474 变为 74 需要减 2 ^ length - 1
            n -= math.pow(2, length-1)
        length -= 1

    print(str)

get_lucky_number(100)