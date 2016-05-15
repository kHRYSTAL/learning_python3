#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""
@version: ??
@usage: 使用特性注解
@author: kHRYSTAL
@license: Apache Licence 
@contact: khrystal0918@gmail.com
@site: https://github.com/kHRYSTAL
@software: PyCharm
@file: 02_use_@property.py
@time: 16/5/15 下午9:20
"""


'在绑定属性时，如果我们直接把属性暴露出去，虽然写起来很简单，但是，没办法检查参数，导致可以把成绩随便改'

class Student(object):
    pass

s = Student()
s.score = 9999

'''
这显然不合逻辑。为了限制score的范围，
可以通过一个set_score()方法来设置成绩，
再通过一个get_score()来获取成绩，这样，在set_score()方法里，
就可以检查参数
'''


class Student(object):
    def get_score(self):
        return self._score
    def set_score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be an integer!')
        if value<0 or value>100:
            raise ValueError('score must between 0 ~ 100')
        self._score = value


s = Student()
s.set_score(60)
print(s.get_score())

# s.set_score(9999)
# Traceback (most recent call last):
#   File "02_use_@property.py", line 49, in <module>
#     s.set_score(9999)
#   File "02_use_@property.py", line 41, in set_score
#     raise ValueError('score must between 0 ~ 100')
# ValueError: score must between 0 ~ 100


'''
有没有既能检查参数，又可以用类似属性这样简单的方式来访问类的变量呢？
对于追求完美的Python程序员来说，这是必须要做到的！

还记得装饰器（decorator）可以给函数动态加上功能吗？
对于类的方法，装饰器一样起作用。
Python内置的@property装饰器就是负责把一个方法变成属性调用的
'''
class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self,value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value




'''
@property的实现比较复杂，我们先考察如何使用。
把一个getter方法变成属性，只需要加上@property就可以了，此时，
@property本身又创建了另一个装饰器@score.setter，
负责把一个setter方法变成属性赋值，于是，我们就拥有一个可控的属性操作：
'''

s = Student()
s.score = 60
print(s.score)

# s.score = 101
# Traceback (most recent call last):
#   File "02_use_@property.py", line 94, in <module>
#     s.score = 101
#   File "02_use_@property.py", line 77, in score
#     raise ValueError('score must between 0 ~ 100!')
# ValueError: score must between 0 ~ 100!



#还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性：

class Student(object):
    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self,birth):
        self._birth = birth

    @property
    def age(self):
        return 2016-self._birth

s = Student()
s.birth = 1990

print(s.age)

'''
上面的birth是可读写属性，而age就是一个只读属性，因为age可以根据birth和当前时间计算出来。

小结

@property广泛应用在类的定义中，可以让调用者写出简短的代码，同时保证对参数进行必要的检查，这样，程序运行时就减少了出错的可能性。

'''

class Screen(object):

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def resolution(self):
        #加下划线调用的是私有属性
        # return self._width * self._height
        #不加下划线调用的是get函数
        return self.height * self.width

screen = Screen()
screen.height = 1080
screen.width = 1920

print(screen.resolution)

def func():
    pass


class Main():
    def __init__(self):
        pass


if __name__ == '__main__':
    pass