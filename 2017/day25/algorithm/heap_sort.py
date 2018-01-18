#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 堆排序
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: heap_sort.py
# @time: 18/1/18 下午3:52
"""
需要先调整成大根堆
即父节点必须比子节点大
每次排序成功后 将根节点移除 从最后一个子节点排到根节点重新调整
"""


def sift(data, low, high):
    """当前的树是乱序的 需要调整成大根堆 父节点一定比子节点值大"""
    i = low  # 根
    j = 2 * i + 1  # 根的左孩子
    tmp = data[i]
    while j <= high:  # high 为右边界
        if j < high and data[j] < data[j + 1]:  # 如果还有右孩子, 且左孩子小于右孩子
            j += 1  # 找到两个孩子中的最大值
        if tmp < data[j]:  # 如果根节点小于孩子中的最大值
            data[i] = data[j]  # 孩子节点上到根节点
            # 子节点作为父节点继续调整当前节点的子节点
            i = j
            j = 2 * i + 1
        else:
            break
    data[i] = tmp  # 将tmp替换到空位


data = list(range(0, 100))
import random
random.shuffle(data)

sift(data, 0, len(data) - 1)
print(data)
