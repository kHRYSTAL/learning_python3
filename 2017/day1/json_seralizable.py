#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: json 序列化
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: json_searlizable.py
# @time: 17/5/30 上午1:09

"""
json 只能定义简单的数据
因为不同语言的数据会存在交互
函数在不同语言中是不同的

如果需要将函数处理为可序列化对象 应使用pickle
"""
import json

info = {
    'name': 'khrystal',
    'age': 22,
}

with open('json.txt', 'w') as f:
    f.write(json.dumps(info))

if __name__ == '__main__':
    pass
