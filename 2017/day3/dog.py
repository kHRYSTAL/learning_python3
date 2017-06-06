#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 面向对象
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: dog.py
# @time: 17/6/6 上午10:51


class Dog:
    def __init__(self, name):
        self.name = name

    def bulk(self):
        print('%s: is bulk' % self.name)


d1 = Dog('1')
d2 = Dog('2')
d3 = Dog('3')
d1.bulk()
d2.bulk()
d3.bulk()
