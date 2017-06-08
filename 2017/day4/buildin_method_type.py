#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: __new__ 对象是类的实例 类是类型的实例 type 是类的类
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: buildin_method_new.py
# @time: 17/6/8 上午10:26


class Foo(object):
    def __init__(self, name):
        self.name = name


f = Foo('alex')

"""
上述代码中, f是通过Foo类实例化的对象
其实 不仅f是一个对象Foo类本身也是一个对象因为在Python中一切事物皆为对象
"""
print(type(f))  # f由Foo类创建
print(type(Foo))  # Foo类由type类创建
print(type(type))  # type 是对象的本源
"""
所以 f对象是Foo类的一个实例, Foo类是type类的一个实例
即: Foo类对象 是通过type类的构造方法创建
"""

"""
第二种创建类的方式
"""


def __init__(self, name, age):
    self.name = name
    self.age = age


def func(self):
    """装配到类的函数"""
    print('hello class %s' % self.name)


'''类名 父类 类的变量和函数'''
Foo = type('Foo', (object,), {'talk': func, '__init__': __init__})
print(type(Foo))
f = Foo('Hello', 22)
f.talk()
