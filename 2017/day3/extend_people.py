#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 多继承
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: people.py
# @time: 17/6/6 下午6:36


class People(object):
    def __init__(self, name):
        self.name = name
        self.friends = []

    def eat(self):
        print('%s is eating' % self.name)


class Relation(object):
    def make_friends(self, obj):
        print('%s is make friend with %s' % (self.name, obj.name))
        self.friends.append(obj)


class Man(People, Relation):
    def __init__(self, name):
        # People.__init__(self, name)
        # Relation.__init__(self)
        super(Man, self).__init__(name)  # 依次调用父类的__init__

    def play(self):
        print('%s is playing' % self.name)


m1 = Man('khrystal')
m2 = Man('jack')

m1.make_friends(m2)
m2.name = 'haha'  # m2在m1的list中
print(m1.friends[0].name)
