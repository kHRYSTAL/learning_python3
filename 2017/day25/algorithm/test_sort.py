#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 测试练习
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: test_sort.py
# @time: 18/2/2 下午5:28

"""
给定一个列表和一个整数, 设计算法找到两个数的下标, 使得两个数之和为给定的整数
保证肯定仅有一个结果

例如 列表[1, 2, 5, 4] 与目标整数3, 1+2=3, 结果为(0, 1)
"""
li = [1, 2, 5, 4]
target = 3


def func1():
    for i in range(len(li)):
        if li[i] > target:
            # 都为正数情况下 sum 值一定比两个数大
            continue
        for j in range(i + 1, len(li)):
            if li[i] + li[j] == target:
                return i, j


print(func1())


def binary_search(data_set, value, low, high):
    while low <= high:
        mid = (low + high) // 2
        if data_set[mid] == value:
            return mid
        elif data_set[mid] > value:
            high = mid - 1
        else:
            low = mid + 1
    return


def func2():
    import copy
    temp_set = copy.deepcopy(li)  # 深复制列表用于排序后通过二分查找快速找到第二个数
    temp_set.sort()
    for i in range(len(temp_set)):
        a = i  # 第一个数的索引
        b = binary_search(temp_set, target - temp_set[a], i + 1, len(temp_set) - 1)  # 通过二分查找找到第二个数
        if b:  # 如果第二个数存在
            return li.index(temp_set[a]), li.index(temp_set[b])  # 返回两个数在原列表的索引


print(func2())


def func3():
    # 设置一个长度为100的列表 用于存储li的下标
    index_data = [None for i in range(100 + 1)]
    for i in range(len(li)):
        index_data[li[i]] = i  # 记录li中每一个值的下标 即把li中index作为value, value作为index
        if index_data[target - li[i]] is not None:  # 如果和为target的另一个值在index-value反向列表中存在 则返回这两个值的value, 即li中的index
            return i, index_data[target - li[i]]

print(func3())


"""
给定一个升序列表和一个整数, 返回该整数在列表中的下标范围
例如 列表[1, 2, 3, 3, 3, 4, 4, 5] 若查找3 则返回(2, 4)
若查找1 则返回(0, 0)
"""


def get_value_scope(data_set, value):
    """
    get index by value, condition is data_set is a sort list
    it is use binary search
    """
    low = 0
    high = len(data_set) - 1
    while low <= high:
        mid = (low + high) // 2
        if data_set[mid] == value:
            # return mid
            left = mid
            right = mid
            while left >= 0 and data_set[left] == value:
                left -= 1
            while right < len(data_set) and data_set[right] == value:
                right += 1
            return left + 1, right - 1
        elif data_set[mid] < value:
            low = mid + 1
        else:
            high = mid - 1
    return


li = [1, 2, 3, 3, 3, 4, 4, 5]
# TODO get value 3 index scope (2, 4)
# print(get_value_scope(li, 5))
