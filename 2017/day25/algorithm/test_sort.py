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


def binary_search(data_set, value):
    """get index by value, condition is data_set is a sort list"""
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
print(binary_search(li, 5))
"""
给定一个升序列表和一个整数, 返回该整数在列表中的下标范围
例如 列表[1, 2, 3, 3, 3, 4, 4, 5] 若查找3 则返回(2, 4)
若查找1 则返回(0, 0)
"""
