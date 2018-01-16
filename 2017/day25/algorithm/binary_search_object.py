#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: binary_search_object.py
# @time: 18/1/15 下午7:44
import random
from faker import Factory

fake = Factory().create('zh_CN')


def random_list(n):
    result = []
    ids = list(range(1001, 1001 + n))
    for i in range(n):
        age = random.randint(18, 60)
        id = ids[i]
        name = fake.name()
        result.append({'id': id, 'name': name, 'age': age})

    return result


def binary_search(data_set, val):
    low = 0
    high = len(data_set) - 1
    while low <= high:
        mid = high - low // 2
        if val == data_set[mid]['id']:
            return data_set[mid]
        elif val > data_set[mid]['id']:
            low = mid + 1
        elif val < data_set[mid]['id']:
            high = mid - 1
    return 'can not find id in data_set'


if __name__ == '__main__':
    i = binary_search(random_list(100), 1099)
    print(i)
