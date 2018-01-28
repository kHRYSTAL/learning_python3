#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 希尔排序
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: shell_sort.py
# @time: 18/1/27 下午11:26
import random


def insert_sort(li, low, high):
    """ 希尔排序每次分组, 每组都要执行一次插入排序 """
    for i in range(low, high + 1):
        tmp = li[i]  # 要执行插入的值
        j = i - 1  # 要插入位置的初始值
        while j >= 0 and li[j] > tmp:  # 有序区从小到大排列, 如果要插入的值小于要插入位置上的值 需要执行插入过程
            li[j + 1] = li[j]  # 有序区右移
            j -= 1  # 要插入位置左移
        li[j + 1] = tmp


def shell_sort(li):
    distance = len(li) // 2
    while distance != 1:
        for i in range(0, distance):
            insert_sort(li, i, distance + i)
        distance //= 2





def insert_sort(li):
    for i in range(1, len(li)):
        # 要插入的值
        temp = li[i]
        # 插入的初始位置
        j = i - 1
        while j >= 0 and li[j] > temp:
            li[j + 1] = li[j]
            li[j] = temp
            j -= 1


data = list(range(10))
random.shuffle(data)
print(data)
insert_sort(data)

print(data)



