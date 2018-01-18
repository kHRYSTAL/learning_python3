#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 快速排序
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: quick_sort.py
# @time: 18/1/18 上午10:29

"""
快速排序
好写的排序算法里最快的
快的排序算法里最好写的

快排思路
取一个元素p(如第一个元素), 使p元素归位
列表被p分为两部分, 左边都比p小, 右边都比p大
递归完成排序
时间复杂度: O(n log n)
"""
import random
import time

import sys

# 设置递归最大层级
sys.setrecursionlimit(10000)


def quick_sort(data, left, right):
    if left < right:  # 至少有两个元素才能执行排序
        mid = partition(data, left, right)  # 把第一个元素放到指定位置, 左边比他小右边比他大, 返回位置index
        quick_sort(data, left, mid - 1)  # 递归mid左侧列表
        quick_sort(data, mid + 1, right)  # 递归mid右侧列表


# 5  7 2 3 9 8   l:0 r:5
# 3  7 2 3 9 8   l:0 r:3
# 3  7 2 7 9 8   l:1 r:3

# 3  2 2 7 9 8   l:1 r:2
# 3  2 5 7 9 8   l:2 r:2
def partition(data, left, right):
    temp = data[left]
    while left < right:
        while left < right and data[right] >= temp:
            right -= 1
        data[left] = data[right]
        while left < right and data[left] <= temp:
            left += 1
        data[right] = data[left]

    data[left] = temp
    return left


data = list(range(1000))
random.shuffle(data)
t1 = time.time()
quick_sort(data, 0, len(data) - 1)
t2 = time.time()
print(t2 - t1)

print(data)
