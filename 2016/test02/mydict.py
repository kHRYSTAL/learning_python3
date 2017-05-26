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
@file: mydict.py
@time: 16/5/17 下午7:27
"""

class Dict(dict):

    def setUp(self):
        print('setUp...')

    def tearDown(self):
        print('tearDown...')

    def __init__(self,**kw):
        super(Dict,self).__init__(**kw)
    def __getattr__(self, item):
        try:
            return self[item]
        except KeyError:
            raise AttributeError(r"Dict' object has no attrbute's %s" % item)

    def __setattr__(self, key, value):
        self[key] = value



def func():
    pass


class Main():
    def __init__(self):
        pass


if __name__ == '__main__':
    pass