#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: [选学]
# @usage: 类的实例化过程
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: class_init_step.py
# @time: 17/6/8 上午10:47


"""
type类如何实现创建类
类是如何创建对象?

类中由一个属性__metaclass__
其用来表示该类由谁来实例化创建
所以 我们可以为__metaclass__设置一个type类的派生类
从而查看类的创建过程
"""


class MyType(type):
    """
    元类的实现 定义自己的类如果创建
    """

    def __init__(cls, what, bases=None, dict=None):
        print('MyType __init__')
        super(MyType, cls).__init__(what, bases, dict)

    def __call__(cls, *args, **kwargs):
        print('MyType __call__')
        obj = cls.__new__(cls, *args, **kwargs)  # 执行Foo的__new__ 获取的obj传给__init__
        # 可以封装一些操作 在obj 创建时
        cls.__init__(obj, *args, **kwargs)  # 执行Foo的__init__


class Foo(object):
    __metaclass__ = MyType  # 默认是type

    def __init__(self, name):
        self.name = name
        print('Foo __init__')

    def __new__(cls, *args, **kwargs):
        """
        cls 为Foo
        类是通过__new__ 实例化的
        内置函数__new__会触发__init__执行
        """
        print('Foo __new__ cls = %s ' % cls, *args, **kwargs)
        # 如果不返回值 对象根本不会实例化
        return object.__new__(cls)  # 调用父类的__new__方法


f = Foo("Foo's Name")
print(f.name)

"""
python3 看不到效果
在2上 流程为
MyType __init__
MyType __call__
Foo __new__
Foo __init__
"""

"""
流程 cls实例化时 通过metaclass 找到元类(默认为Type)
type = Type() 实例化
type() 调用 __call__方法执行 cls的__new__(), __init__()
"""

"""
元类的作用 定制一个类(在类创建前初始化一些操作) 一般用不到
"""
