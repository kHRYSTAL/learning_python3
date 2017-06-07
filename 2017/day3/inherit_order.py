#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 继承顺序
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: inherit_order.py
# @time: 17/6/7 上午10:38

"""
多继承的函数 横向查找 使用广度优先算法 而不是查找不到去找父类(深度优先)[python2 是深度优先]
"""


class A(object):
    def __init__(self):
        print('A')


class B(A):
    def __init__(self):
        print('B')


class C(A):
    def __init__(self):
        print('C')


class D(B, C):
    def __init__(self):
        super(D, self).__init__()  # [多继承按从左到右的顺序执行][如果B和C中有相同的函数 则执行完B 不会执行C]
        # B.__init__(self) # 执行B后执行C
        # C.__init__(self)


D()
