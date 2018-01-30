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


def top_sort(li, top_value):
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

data = [i for i in range(1000)]
random.shuffle(data)
print(data)
result = top_sort(data, 10)
print(result)

