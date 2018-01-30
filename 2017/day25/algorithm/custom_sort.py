#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: test.py
# @time: 18/1/29 下午7:09
"""
现在有一个列表,列表中的数范围都在0-100之间, 列表长度大约为100万
设计算法在O(n)时间复杂度内将列表进行排序
注意: 此中排序 都需要有条件限制 否则不可能达到O(n)
"""


def count_sort(li, max_num):
    """
    创建一个列表, 用来统计每个数出现的次数
    """
    count = [0 for i in range(max_num + 1)]
    for num in li:
        count[num] += 1
    # count 列表index为li列表上的数值, 列表的item表示出现的次数
    i = 0
    for index, item in enumerate(count):
        for j in range(item):
            li[i] = index
            i += 1


import random

# data = []
# for i in range(10000):
#     data.append(random.randint(0, 100))
# print(data)
# count_sort(data, 100)
# print(data)

"""
现在有n个数(n > 100000), 设计算法, 按大小顺序得到前10大的数
应用场景 榜单top 10
相当于插入排序 当插到的值达到10, 不需要进行后续的插入
"""


def insert_sort(li):
    for i in range(1, len(li)):
        # 要插入的值
        temp = li[i]
        # 插入的初始位置
        j = i - 1
        while j >= 0 and li[j] < temp:
            li[j + 1] = li[j]
            li[j] = temp
            j -= 1


def top_sort_by_insert(li, top_value):
    # 最终返回结果
    res = li[0: top_value + 1]
    # 先排序一次
    insert_sort(res)
    for i in range(top_value + 1, len(li)):
        temp = li[i]  # 要插入的值
        j = top_value - 1  # 要插入的初始位置
        while j >= 0 and res[j] < temp:
            res[j + 1] = res[j]
            res[j] = temp
            j -= 1

    return res[0: -1]


# data = [i for i in range(1000)]
# random.shuffle(data)
# print(data)
# result = top_sort_by_insert(data, 10)
# print(result)


def sift(data, low, high):
    """调整函数 生成小根堆 即根的值在堆中最小"""
    i = low  # 父
    j = 2 * i + 1  # 父的左孩子
    tmp = data[i]
    while j <= high:  # high 为右边界
        if j + 1 <= high and data[j] > data[j + 1]:  # 如果还有右孩子, 且左孩子大于右孩子
            j += 1  # 找到两个孩子中的最小值的index

        if tmp > data[j]:  # 如果父节点大于孩子中的最小值
            data[i] = data[j]  # 孩子节点上到父节点
            # 下移一层
            i = j
            j = 2 * i + 1
        else:
            break
    data[i] = tmp  # 将tmp替换到空位


def top_sort_by_heap(li, top_value):
    heap = li[0:top_value]
    for i in range(top_value // 2 - 1, -1, -1):
        sift(heap, i, top_value - 1)  # 调整每个父节点,使heap成为小根堆

    # 遍历除heap外的其他元素
    for i in range(top_value, len(li)):
        if li[i] > heap[0]:  # 如果当前元素比根节点大, 进行替换
            heap[0] = li[i]
            sift(heap, 0, top_value - 1)  # 调整

    # print(heap)
    for i in range(top_value - 1, -1, -1): # 每次把最小值(根)移动到列表最后,使其不参与调整 最终使heap有序
        heap[0], heap[i] = heap[i], heap[0]
        sift(heap, 0, i - 1)
        # print(heap)
    return heap


data = [i for i in range(100)]
random.shuffle(data)
print(data)
result = top_sort_by_heap(data, 10)
print(result)
