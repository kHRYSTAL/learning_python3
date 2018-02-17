#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: queue.py
# @time: 18/2/17 下午11:08


from collections import deque

queue = deque()

queue.append(1)
queue.append(2)
print(queue.popleft())