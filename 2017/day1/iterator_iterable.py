#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: iterator_iterable.py
# @time: 17/5/26 下午7:33
"""
可迭代对象:
1.集合 字符串等
2.生成器

迭代器:
可以按照一定规则排序 且能按照规则知道下个元素的值 惰性的
生成器, 文件流 等
集合不是迭代器 带可以通过iter(arg) 成为迭代器
range(arg) 在3.x 中是迭代器 在 2.x中是列表

for 循环支持的必须是可迭代对象
注意: 不要在列表for 循环的时候进行增删操作 因为for循环会生成迭代器去进行iter
改变数据内部元素会导致next顺序改变

因此 在处理时应对列表进行全拷贝 for i in l[:] 再进行处理
"""

from collections import Iterable, Iterator

l = [x for x in range(10)]
print(l)

print(isinstance(l, Iterable))
print(isinstance(l, Iterator))
l = iter(l)
print(isinstance(l, Iterator))

if __name__ == '__main__':
    pass