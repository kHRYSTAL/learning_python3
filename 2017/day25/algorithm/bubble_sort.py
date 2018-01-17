#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 冒泡排序
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: bubble_sort.py
# @time: 18/1/17 下午2:51
"""
1~9 乱序排列的n个数
从小到大排序时
第1次需要排序9-1次 找到最大值9
第2次需要排序9-2次 找到最大值9-1
...
第8次需要排序9-8次 找到最大值9-8
"""
import random
import time


def cost(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        func(*args, **kwargs)
        t2 = time.time()
        print(t2 - t1)

    return wrapper


@cost
def bubble_sort(li):
    for i in range(len(li) - 1):  # 需要排序的轮次数
        for j in range(len(li) - i - 1):  # 每个轮次需要排序几次
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]  # 按照升序排列, 如果前面的数比后面的数大, 交换位置


data = list(range(1000))
random.shuffle(data)
bubble_sort(data)
print(data)
