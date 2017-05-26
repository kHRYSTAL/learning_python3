#!/usr/bin/env python3
#-*- coding:utf-8 -*-

'''
可以直接作用于for循环的对象统称为可迭代对象：Iterable。
'''
'''
一类是集合数据类型，如list、tuple、dict、set、str等；

一类是generator，包括生成器和带yield的generator function。
'''

'''
可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。
'''

from collections import Iterator

isinstance((x for x in range(10)),Iterator)

isinstance([],Iterator)#false
isinstance({},Iterator)#false
isinstance('abc',Iterator)#false

#把list、dict、str等Iterable变成Iterator可以使用iter()函数：

isinstance(iter([]),Iterator)
isinstance(iter('abc'),Iterator)
isinstance(iter({}),Iterator)

'''
Iterator对象表示的是一个数据流，Iterator对象可以被next()函数调用并不断返回下一个数据，
直到没有数据时抛出StopIteration错误。可以把这个数据流看做是一个有序序列，
但我们却不能提前知道序列的长度，只能不断通过next()函数实现按需计算下一个数据，所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算。
'''

for x in [1, 2, 3, 4, 5]:
    pass

it = iter([1, 2, 3, 4, 5])
# 循环:
while True:
    try:
        # 获得下一个值:
        x = next(it)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break