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
第1次[外层循环]需要排序9-1次[内层循环] 找到最大值9
第2次需要排序9-2次 找到最大值9-1
...
第8次需要排序9-8次 找到最大值9-8

冒泡排序每次都是两两比较 最后选出一个最大值冒出去
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
        exchange = False
        for j in range(len(li) - i - 1):  # 每个轮次需要排序几次
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]  # 按照升序排列, 如果前面的数比后面的数大, 交换位置
                exchange = True
        if not exchange:  # 如果没有发生交换,说明已经排序好了,不需要在重复比较之后的轮次
            break


"""
选择排序
每次全部遍历记录最小的数 放到第一个位置
在一趟遍历记录剩余列表中最小的数
问题是 怎么选出最小的数
与冒泡排序不同的是 选择排序并不是两两交换后执行下次比较
而是找到最小值 直接与第一个数替换位置
"""


@cost
def select_sort(li):
    for i in range(len(li) - 1):  # 需要遍历的轮次
        min_index = i  # 第一次是0 第二次从1开始
        for j in range(i, len(li)):  # 每个轮次需要比较的次数
            if li[j] < li[min_index]:
                min_index = j
        li[i], li[min_index] = li[min_index], li[i]  # 直接与第一个数交换位置


"""
插入排序
列表分为有序区和无序区两个部分 最初有序区只有一个元素
每次从无序区选择一个元素插入到有序区的位置
直到无序区变空
"""


@cost
def insert_sort(li):
    for i in range(1, len(li)):
        tmp = li[i]  # 要执行插入的值
        j = i - 1  # 要插入位置的初始值
        while j >= 0 and li[j] > tmp:  # 有序区从小到大排列, 如果要插入的值小于要插入位置上的值 需要执行插入过程
            li[j + 1] = li[j]  # 有序区右移
            j -= 1  # 要插入位置左移
        li[j + 1] = tmp


data = list(range(1000))
random.shuffle(data)
bubble_sort(data)

data_1 = list(range(1000))
random.shuffle(data_1)
select_sort(data_1)

data_2 = list(range(1000))
random.shuffle(data_2)
insert_sort(data_2)

print(data)
print(data_1)
