#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 断言
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: assert_module.py
# @time: 17/6/11 上午1:44


class C(object):
    def __init__(self):
        self.name = 'khrystal'

obj = C()
assert type(obj.name) is str
print('assert is success')

assert type(obj.name) is int
print('assert is failed')


if __name__ == '__main__':
    pass
