#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: read_csv.py
# @time: 17/8/24 下午4:58


import csv


def handle_csv(del_row):
    with open('tracker.csv', 'r', encoding='utf8') as f, open('new_tracker.csv', 'w+', encoding='utf8') as new_f:
        old_csv = csv.reader(f)
        new_csv = csv.writer(new_f)
        rows = [row for row in old_csv]
        print(rows)
        for index in del_row:
            print(index)
            rows.remove(rows[index])
        new_csv.writerows(rows)


handle_csv([0, ])
