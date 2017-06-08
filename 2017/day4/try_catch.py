#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 异常处理
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: try_catch.py
# @time: 17/6/8 下午3:25


class Dog(object):
    def __init__(self, name):
        self.name = name

    def eat(self):
        print('%s is eating...')


d = Dog('dog')
# choice = input('>>:').strip()
# getattr(d, choice)  # 'Dog' object has no attribute 'dd'

data = {}
names = ['alex', 'jack']
try:
    # data['name']  # KeyError: 'name'
    # names[3]  # list index out of range
    a = 1  # 正常操作
except KeyError as e:
    print('没有这个key:', e)
except IndexError as e:
    print('数组越界:', e)
except Exception as e:
    print('统一处理,', e)
else:
    print("没有出错 一切正常")
finally:
    print('finally 有没有错都执行')

try:
    open('test.txt')
except FileNotFoundError as e:
    print(e)

