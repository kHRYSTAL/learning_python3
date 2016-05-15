#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""
@version: ??
@usage: 
@author: kHRYSTAL
@license: Apache Licence 
@contact: khrystal0918@gmail.com
@site: https://github.com/kHRYSTAL
@software: PyCharm
@file: 01_use__slots__.py
@time: 16/5/15 下午9:11
"""

class Student(object):
    pass


s = Student();
s.name = 'Matt'
print(s.name)

#给实例绑定方法

def set_age(self, age):
    self.age = age

from types import MethodType
s.set_age = MethodType(set_age, s)

s.set_age(25)
print(s.age)

#但是，给一个实例绑定的方法，对另一个实例是不起作用的：

s2 = Student()
#s2.set_age(22)
# File "01_use__slots__.py", line 39, in <module>
#    s2.set_age(22)
#AttributeError: 'Student' object has no attribute 'set_age'

#为了给所有实例都绑定方法，可以给class绑定方法

def set_score(self,score):
    self.score = score

Student.set_score = set_score

s = Student()
s.set_score(99)
print(s.score)

s2 = Student()
s2.set_score(88)
print(s2.score)


'''
    使用__slots__

但是，如果我们想要限制实例的属性怎么办？比如，只允许对Student实例添加name和age属性。

为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性：
'''

class Student(object):
    __slots__ = ('name', 'age')


s = Student()

s.name = 'Matt'
s.age = 25

# s.score = 99
# Traceback (most recent call last):
#   File "01_use__slots__.py", line 77, in <module>
#     s.score = 99
# AttributeError: 'Student' object has no attribute 'score'


'''
由于'score'没有被放到__slots__中，所以不能绑定score属性，试图绑定score将得到AttributeError的错误。

使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：
'''

class GraduateStudent(Student):
    pass

g = GraduateStudent()

g.score = 99
print(g.score)




def func():
    pass


class Main():
    def __init__(self):
        pass


if __name__ == '__main__':
    pass