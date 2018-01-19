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
import random
import time


def cost_time(func):
    def wrapper(*args, **kwargs):
        before = time.time()
        x = func(*args, **kwargs)
        after = time.time()
        print(after - before, func.__name__)
        return x

    return wrapper


def sift(data, low, high):
    """调整函数"""
    i = low  # 父
    j = 2 * i + 1  # 父的左孩子
    tmp = data[i]
    while j <= high:  # high 为右边界
        if j + 1 <= high and data[j] < data[j + 1]:  # 如果还有右孩子, 且左孩子小于右孩子
            j += 1  # 找到两个孩子中的最大值的index

        if tmp < data[j]:  # 如果父节点小于孩子中的最大值
            data[i] = data[j]  # 孩子节点上到父节点
            # 下移一层
            i = j
            j = 2 * i + 1
        else:
            break
    data[i] = tmp  # 将tmp替换到空位

@cost_time
def heap_sort(data):
    length = len(data)
    # 指定第一个进行调整的元素的下标
    # 它即该无序序列完全二叉树的第一个非叶子节点
    # 它之前的元素均要进行调整
    first_exchange_element = length // 2 - 1
    # 当前非叶子节点开始 到根节点 遍历所有节点, 每次都进行调整
    for i in range(first_exchange_element, -1, -1):
        sift(data, i, length - 1)

    # 将根节点放到最终位置，剩余无序序列继续堆排序
    # length-1 次循环完成堆排序
    for i in range(length - 1, -1, -1):
        data[0], data[i] = data[i], data[0]
        # 放到最后的最大值 不需要参与调整了
        sift(data, 0, i - 1)


data = list(range(0, 100))
random.shuffle(data)
heap_sort(data)
print(data)
