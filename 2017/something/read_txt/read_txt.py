#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: read_txt.py
# @time: 17/8/3 下午11:12

with open('text.txt', 'r', encoding='utf8') as f:
    for line in f:
        print(line)

if __name__ == '__main__':
    pass