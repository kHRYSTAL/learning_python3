#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 属性方法
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: perproty_method.py
# @time: 17/6/7 下午4:35


class Dog(object):
    def __init__(self, name):
        self.name = name

    @property
    def eat(self):
        """
        属性方法
        将函数转换为对象的一个静态属性
        """
        print('%s is eating' % (self.name,))


# d = Dog('dog')
# # d.eat()  # 'NoneType' object is not callable
# d.eat  # property 将函数转换为对象的一个属性

"""
属性方法设置参数
"""


class Cat(object):
    def __init__(self, name):
        self.name = name
        self.__food = None

    @property
    def eat(self):
        print('%s is eating' % self.name)
        return self.__food

    @eat.setter
    def eat(self, food):
        """
        属性方法支持set参数
        """
        print('set food %s' % food)
        self.__food = food

    @eat.getter
    def eat(self):
        """
        属性方法get, 如果增加该方法 eat的属性方法不能再执行
        因为函数名相同 按上下顺序被覆盖
        """
        return self.__food

    @eat.deleter
    def eat(self):
        """
        删除属性
        """
        del self.__food
        print('del __food')


c = Cat('cat')

c.eat = 'mouse'

print(c.eat)

del c.eat
