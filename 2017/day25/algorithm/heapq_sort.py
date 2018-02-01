#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 通过内置模块heapq实现堆排序
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: heapq_sort.py
# @time: 18/2/1 下午4:15
from heapq import heappush, heappop
import random


def heapq_sort(li):
    h = []
    for value in li:
        heappush(h, value)
    return [heappop(h) for i in range(len(h))]


data = [i for i in range(100)]
random.shuffle(data)
print(data)
result = heapq_sort(data)
print(result)
