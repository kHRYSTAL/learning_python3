#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: pickle 反序列化
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: pickle_deseralizable.py
# @time: 17/5/30 上午1:36

import pickle


def func(name):
    print('序列化的是函数名')


data = None
with open('pickle.txt', 'rb') as f:
    data = pickle.loads(f.read())

print(data)
data['func']('')
