#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: class_bulid_method.py
# @time: 17/6/7 下午10:10
"""
__doc__ 输出类注释
__module__ 表示当前操作的对象在哪个模块
__class__ 表示当前操作的对象是哪个类
__call__ 触发构造方法 对象 ＝ 类名()，对于__call__方法的执行是由对象加()触发的
         即:对象() 或类()()
__dict__ 查看类或对象中所有成员
__str__ 打印时调用
"""


class Dog(object):
    """
    这个注释可以用__doc__查看
    """

    def __call__(self, *args, **kwargs):
        print('execute dog call!', args, kwargs)

    def __str__(self):
        return 'this is str return name'


# region __doc__
print(Dog.__doc__)
# endregion

# region __module__
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
import sys

sys.path.append(BASE_DIR)
from class_build_method.aa import C

obj = C()

print(obj.__module__)
# endregion

# region __class__
print(obj.__class__)
# endregion

# region __call__
d = Dog()
d(1, 2, 3, name=333)
# endregion

# region __dict__
d.name = 'Dog'
print(d.__dict__)
print(Dog.__dict__)
# endregion

# region __str__
print(d)
# endregion
