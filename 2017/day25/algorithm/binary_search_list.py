#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 二分查找 不使用切片 因为切片有O(1)的时间复杂度
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: binary_search.py
# @time: 18/1/15 下午6:36
import time


def cost_time(func):
    def wrapper(*args, **kwargs):
        before = time.time()
        x = func(*args, **kwargs)
        after = time.time()
        print(after - before, func.__name__)
        return x

    return wrapper


@cost_time
def binary_search(data_list, val):
    low = 0
    high = len(data_list) - 1
    while low <= high:
        mid = (low + high) // 2  # 整除
        if data_list[mid] == val:
            return mid
        elif data_list[mid] < val:
            low = mid + 1
        else:
            high = mid - 1
    return "can not find index in list"


if __name__ == '__main__':
    i = binary_search(list(range(10)), 2)
    print(i)
    i = binary_search(list(range(10)), 11)
    print(i)
