#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: singleton_test.py
# @time: 18/1/4 下午1:43


class Foo(object):
    def __init__(self):
        pass

    def process(self):
        return '123'


print("非单例")
obj1 = Foo()
print(id(obj1))
obj2 = Foo()
print(id(obj2.process()))


# 通用操作封装在对象中, 占用的内存大 应该使用单例模式

class Boo(object):
    # 静态字段 只属于类 且只存在一份
    instance = None

    """ 第一种单例模式 """

    def __init__(self):
        pass

    @classmethod
    def get_instance(self):
        """ 类方法 不需要实例化 """
        if Boo.instance:
            return Boo.instance
        else:
            Boo.instance = Boo()
            return Boo.instance

    def process(self):
        return '123'


print('单例')
obj1 = Boo.get_instance()
print(id(obj1))
obj2 = Boo.get_instance()
print(id(obj2))


# 第二种方式

class Poo(object):
    instance = None

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        # # 默认实现方法 内部会执行Poo.__init__
        # obj = object.__new__(cls, *args, **kwargs)
        # return obj
        if Poo.instance:
            return Poo.instance
        else:
            Poo.instance = object.__new__(cls, *args, **kwargs)
            return Poo.instance


print('单例2')

obj1 = Poo()
print(id(obj1))
obj2 = Poo()
print(id(obj2))