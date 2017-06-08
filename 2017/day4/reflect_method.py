#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 反射
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: reflect_method.py
# @time: 17/6/8 下午2:03


class Dog(object):
    def __init__(self, name):
        self.name = name

    def eat(self):
        print('%s is eating...' % self.name)


def bulk(self):
    """
    需要增加到对象中的方法
    """
    print('%s is yelling' % self.name)


"""
通过函数名反射执行函数
hasattr(obj, var_name) 判断一个对象是否有对应的字符串的方法映射
getattr(obj, var_name) 通过字符串获取对象内部指定方法的内存地址
setattr(obj, var_name, value) 设置对象的变量名称和 函数或变量的值 obj.var_name = value
delattr(obj, var_name) 删除变量 相当于 del obj.var_name

"""
d = Dog('Dog')
choice = input('>>:').strip()

# # 判断输入的字符串是否为d中的函数
# print(hasattr(d, choice))
# # 获取函数内存地址
# print(getattr(d, choice))
# # 执行函数
# getattr(d, choice)()

# if d.__getattribute__(choice):
#     d.eat()


if hasattr(d, choice):  # func存在则调用
    attr = getattr(d, choice)
    if type(attr) is str:  # 如果是字符串变量
        print(attr)
        delattr(d, choice)  # 删除字符串变量
    else:  # 如果是func
        attr()  # 如果func有参数 可以在这里添加
else:  # func或变量 不存在 增加
    setattr(d, choice, bulk)  # 将bulk增加到d中 第二个参数为varName 第三个参数为变量(函数)的内存地址
    func = getattr(d, choice)  # 调用函数
    func(d)

print(d.name)  # 如果输入的是name 则在上方代码已经删除 此处会报错 'Dog' object has no attribute 'name'
