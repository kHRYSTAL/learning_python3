#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 列表生成式
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: generator_list.py
# @time: 17/5/26 下午7:37

l = [x*2 for x in range(10)]
print(l)

g = (x*2 for x in range(10))
print(g)

if __name__ == '__main__':
    pass