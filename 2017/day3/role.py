#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 构造函数 类变量 析构函数
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: role.py
# @time: 17/6/6 上午11:50


class Role(object):
    n = 123  # 类变量相当于java的静态全局变量 不实例化也可以调用 但基本类型不同对象修改 值也会不同
    n_list = []

    def __init__(self, name, role, weapon, life_value=100, money=15000):
        """
        构造函数 在实例化时调用 做一些类的初始化操作
        """
        self.name = name  # 实例变量不实例化不存在
        self.role = role
        self.weapon = weapon
        self.life_value = life_value
        self.__money = money  # 私有变量不可直接访问

    def __shot(self):
        """
        私有方法 不可直接调用
        """
        print('shooting...')

    def got_shot(self):
        print('ah..., I got shot...')

    def buy_gun(self, gun_name):
        print('%s just bought %s' % (self.name, gun_name))

    def __del__(self):
        """
        析构函数
        """
        print('%s is dead' % self.name)


print(Role)
# print(Role.shot())
r1 = Role('Alex', 'police', 'AK47')  # 创建一份内存拷贝至r1指向的内存地址
r2 = Role('Jack', 'terrorist', 'B22')  # 创建一份内存拷贝至r2指向的内存地址

# 等价操作
r1.buy_gun('51')
Role.buy_gun(r1, '51')

# 外部新增变量
r1.test = 1
print(r1.test)
# print(r2.test)  # r2 没有该引用

"""
类变量 如果找不到对象的变量 则会去找类变量
"""
# 如果修改的n n为栈内存变量(基本类型) 则修改的不是同一份
r1.n = 234
print(Role.n)
print(r1.n, r1.name)
print(r2.n, r2.name)

# 如果修改的是对象 那么所有的对象都会改变 在堆内存中 修改的是同一份Role.n_list 的内存地址
# 因此在日常操作中 最好将类变量认为是java中的静态变量 对象的变量变量都使用实例变量赋值
r1.n_list.append('from r1')
r2.n_list.append('from r2')
print(Role.n_list)
print(r1.n_list)
print(r2.n_list)

# 类变量的用途 所有对象公用的属性 节省开销和内存

"""
析构函数:
在实例释放 销毁的时候执行的 通常用于做一些收尾工作
关闭一些如:
    数据库链接/打开的临时文件
"""
del r2  # 优先执行r2 析构函数
