#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 多态 一个接口多个实现 (接口的重用)
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: polymorphic.py
# @time: 17/6/7 下午12:02

"""
python 中没有直接的语法实现多态 但是可以在父类中定义方法去实现多态
(可添加静态装饰器去指明 类可以直接调用该方法 类似Java的静态方法)
去实现鸭子类型(接口的实现)
"""


class Animal:
    def __init__(self, name):  # Constructor of the class
        self.name = name

    def talk(self):
        pass

    @staticmethod
    def animal_talk(obj):
        """
        该函数为接口 一个接口多种实现
        """
        print(obj.talk())


class Cat(Animal):
    def talk(self):
        return 'Meow!'


class Dog(Animal):
    def talk(self):
        return 'Woof! Woof!'


d = Dog('dog')
# print(d.talk())
c = Cat('cat')
# print(c.talk())

Animal.animal_talk(d)
Animal.animal_talk(c)
