#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: json_desearlizable.py
# @time: 17/5/30 上午1:17
import json

data = None

with open('json.txt', 'r') as f:
    data = f.read()

print(data)  # 此时是字符串
data = json.loads(data)  # 反序列化

print(data['name'])
print(data['age'])

if __name__ == '__main__':
    pass
