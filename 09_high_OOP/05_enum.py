#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""
@version: ??
@usage: 枚举
@author: kHRYSTAL
@license: Apache Licence 
@contact: khrystal0918@gmail.com
@site: https://github.com/kHRYSTAL
@software: PyCharm
@file: 05_enum.py
@time: 16/5/16 下午10:31
"""
from enum import Enum

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
    print(name,'=>',member,',',member.value)


'''
value属性则是自动赋给成员的int常量，默认从1开始计数。

如果需要更精确地控制枚举类型，可以从Enum派生出自定义类：
'''

from enum import Enum,unique

@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

'''
@unique装饰器可以帮助我们检查保证没有重复值。

访问这些枚举类型可以有若干种方法：
'''

day1 = Weekday.Mon
print(day1)
print(Weekday.Thu)
print(Weekday['Tue'])

print(Weekday.Fri.value)
print(day1 == Weekday.Mon)
print(Weekday(1))
print(day1==Weekday(1))
'''
Weekday(7)
Traceback (most recent call last):
  ...
ValueError: 7 is not a valid Weekday
'''

for name , member in Weekday.__members__.items():
    print(name,'=>',member,'=>',member.value)


'Enum可以把一组相关常量定义在一个class中，且class不可变，而且成员可以直接比较。'


def func():
    pass


class Main():
    def __init__(self):
        pass


if __name__ == '__main__':
    pass