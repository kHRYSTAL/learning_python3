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


data = [1, 1, 1, 3, 4, 5, 1, 2, 4, 5, 6, 9, 7, 7, 2, 3, 4, 4]
import random
random.shuffle(data)
count_sort(data, 9)
print(data)