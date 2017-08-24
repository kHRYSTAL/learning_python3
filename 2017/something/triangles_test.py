#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 用python 输出杨辉三角 每行为一个list
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: triangles_test.py
# @time: 17/6/25 下午11:21


def tri():
    a = [1]
    while True:
        yield a
        a = [sum(i) for i in zip([0] + a, a + [0])]

if __name__ == '__main__':
    g = tri()
    for x in range(10):
        print(next(g))
