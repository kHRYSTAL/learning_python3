#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 静态方法 和 类方法
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: static_method.py
# @time: 17/6/7 下午3:57


class Dog(object):
    name = 'khrystal'

    def __init__(self, name):
        self.name = name

    @staticmethod
    def eat(dog_obj, food):
        """
        静态方法不会自动传Self 应使用类名调用
        静态方法与实例化的对象实际上没有关系了
        """
        print('%s is eating %s' % (dog_obj.name, food))

    @classmethod
    def talk(self):
        """
        类方法: 只能调用类变量 实例变量不能调用 基本没用
        用途: 比如实例变量和类变量有重名情况 需要强制调用类变量 可以使用类方法
        """
        print('%s is talking' % self.name)

d = Dog('dog')

# 静态方法调用
Dog.eat(d, 'shit')

# 类方法调用
d.talk()
