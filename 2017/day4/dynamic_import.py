#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: dynamic_import.py
# @time: 17/6/11 上午12:37

# import lib.aa as module
# # obj = module.C('khrystal')
# instance = getattr(module, 'C')
# obj = instance('khrystal')
# print(obj.name)

module = __import__('lib.aa')
"""
import lib 是导入 __init__
import lib.aa 如果不设置别名 无法调用
from lib import aa 可以调用aa.*
"""
print(module.aa)  # 打印可以看出, 实际上得到的是lib模块而不是aa模块 所以需要加上aa
"""
如果__import__('lib)
实际上找的是__init__.py文件里的变量
"""
obj = module.aa.C('khrystal')
print(obj.name)

# instance = getattr(module.aa, 'C')  # 反射获取类, 如果是通过动态方法获取, 需要加上文件名
# obj = instance('khrystal')
# print(obj.name)


import importlib

lib = importlib.import_module('lib.aa')  # 建议使用
print(lib)
print(lib.C('khrystal').name)
