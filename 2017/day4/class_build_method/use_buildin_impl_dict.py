#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 通过内置方法实现一个像字典的对象
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: class_build_method2.py
# @time: 17/6/7 下午10:35
"""
__getitem__
__setitem__
__delitem__
"""


class Foo(object):

    def __init__(self):
        self.data = {}

    def __getitem__(self, key):
        print('__getitem__', key)
        return self.data[key]

    def __setitem__(self, key, value):
        print('__setitem__', key, value)
        self.data[key] = value

    def __delitem__(self, key):
        print('__delitem__', key)
        del self.data[key]


obj = Foo()

# region call __setitem__
obj['name'] = 'alex'
# endregion

# region call __getitem__
print(obj['name'])
# endregion

# region call __delitem__
del obj['name']
# endregion

