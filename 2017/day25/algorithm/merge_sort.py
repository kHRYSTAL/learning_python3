#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 一次归并排序
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: merge_sort.py
# @time: 18/1/25 下午7:02

"""
2 5 7 8 9(mid) 1 3 4 6
"""


def merge(li, low, mid, high):
    """
    一次归并排序
    如果有一段序列最后有剩余值
    需要再执行一次归并排序
    """
    i = low
    j = mid + 1  # 第二段有序列表的第一个值
    ltmp = []
    while i <= mid and j <= high:  # 保证两段序列都有数
        if li[i] < li[j]:
            ltmp.append(li[i])
            i += 1
        else:
            ltmp.append(li[j])
            j += 1

    while i <= mid:  # 左边数值有剩余
        ltmp.append(li[i])
        i += 1
    while j <= high:  # 右边数值有剩余
        ltmp.append(li[j])
        j += 1

    li[low: high+1] = ltmp


def merge_sort(li, low, high):
    if low < high:
        # 将无序列表拆分至单个元素 每两个元素进行比较排序
        mid = (low + high) // 2
        merge_sort(li, low, mid)
        merge_sort(li, mid + 1, high)
        merge(li, low, mid, high)


import random
data = list(range(0, 10))
random.shuffle(data)
print(data)
merge_sort(data, 0, len(data) - 1)
print(data)

