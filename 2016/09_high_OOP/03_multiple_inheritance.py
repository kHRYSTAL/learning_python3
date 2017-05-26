#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""
@version: ??
@usage: 多重继承
@author: kHRYSTAL
@license: Apache Licence 
@contact: khrystal0918@gmail.com
@site: https://github.com/kHRYSTAL
@software: PyCharm
@file: 03_ multiple_inheritance.py
@time: 16/5/15 下午9:41
"""

class Animal(object):
    pass

#哺乳类
class Mammal(Animal):
    pass

class Bird(Animal):
    pass

class Dog(Mammal):
    pass

class Bat(Mammal):
    pass

#鹦鹉
class Parrot(Bird):
    pass

#鸵鸟
class Ostrich(Bird):
    pass

class Runnable(object):
    def run(self):
        print("Running...")

class Flyable(object):
    def fly(self):
        print("Flying...")

class Dog(Mammal, Runnable):
    pass

class Bat(Mammal, Flyable):
    pass

#通过多重继承，一个子类就可以同时获得多个父类的所有功能。

#MixIn
#在设计类的继承关系时，通常，主线都是单一继承下来的，
# 例如，Ostrich继承自Bird。但是，如果需要“混入”额外的功能，
# 通过多重继承就可以实现，比如，让Ostrich除了继承自Bird外，
# 再同时继承Runnable。这种设计通常称之为MixIn。

#肉食
class CarnivorousMixIn(object):
    def canEatMeat(self):
        print("Carnivorous")

class Dog(Mammal, Runnable, CarnivorousMixIn):
    pass


'''
Python自带的很多库也使用了MixIn。举个例子，Python自带了TCPServer和UDPServer这两类网络服务，
而要同时服务多个用户就必须使用多进程或多线程模型，
这两种模型由ForkingMixIn和ThreadingMixIn提供。
通过组合，我们就可以创造出合适的服务来。
'''

'''
比如，编写一个多进程模式的TCP服务，定义如下：

class MyTCPServer(TCPServer, ForkingMixIn):
    pass
编写一个多线程模式的UDP服务，定义如下：

class MyUDPServer(UDPServer, ThreadingMixIn):
    pass
如果你打算搞一个更先进的协程模型，可以编写一个CoroutineMixIn：

class MyTCPServer(TCPServer, CoroutineMixIn):
    pass
'''


'''
由于Python允许使用多重继承，因此，MixIn就是一种常见的设计。

只允许单一继承的语言（如Java）不能使用MixIn的设计。
'''



##问题

class A(object):
    def run(self):
        print('Running A')
class B(object):
    def run(self):
        print('Running B')

class C(A,B):
    pass

c = C()
c.run()

#优先级是继承的首个父类的方法，在有共同方法的时候。

def func():
    pass


class Main():
    def __init__(self):
        pass


if __name__ == '__main__':
    pass