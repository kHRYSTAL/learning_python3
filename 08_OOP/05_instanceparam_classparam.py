#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""
@version: ??
@usage: 实例属性和类属性
@author: kHRYSTAL
@license: Apache Licence 
@contact: khrystal0918@gmail.com
@site: https://github.com/kHRYSTAL
@software: PyCharm
@file: 05_instanceparam_classparam.py
@time: 16/5/15 下午8:42
"""

class Student(object):
    def __init__(self, name):
        self.name = name

'''
根据类创建的实例可以任意绑定属性。

给实例绑定属性的方法是通过实例变量，或者通过self变量
'''
s = Student('Bob')
s.score = 90

'''
但是，如果Student类本身需要绑定一个属性呢？
可以直接在class中定义属性，这种属性是类属性，归Student类所有
'''

class Student(object):
    name = 'Student'

s = Student()
print(s.name)

print(Student.name)#类属性可以直接调用
s.name = 'Matt'#给实例绑定属性 如果名称相同 会屏蔽类属性 因为实例属性优先级高
print(s.name)

del s.name #删除实例属性
print(s.name)












def func():
    pass


class Main():
    def __init__(self):
        pass


if __name__ == '__main__':
    pass