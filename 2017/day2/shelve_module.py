#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: k-v模式的pickle封装 类似sharedpreference
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: shelve_module.py
# @time: 17/6/5 上午10:54

import shelve
import datetime
"""
写
"""
# d = shelve.open('shelve_test')
# info = {'age': 22, 'job': 'it'}
#
# name = ['alex', 'rain', 'test']
# d['name'] = name  # 持久化列表
# d['info'] = info  # 持久化字典
# d['data'] = datetime.datetime.now()
# d.close()

"""
读
"""
d = shelve.open('shelve_test')
print(d.get('name'))
print(d.get('info'))
print(d.get('data'))
d.close()

