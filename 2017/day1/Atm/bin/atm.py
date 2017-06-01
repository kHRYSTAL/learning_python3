#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: atm.py
# @time: 17/5/31 上午12:10

# print('Welcome to my Application')
import os
import sys

# print(__file__)  # 打印的是相对路径但在pycharm是从根目录开始查找的
# print(os.path.abspath(__file__))  # 通过相对路径自动获取绝对路径
#
# print(os.path.dirname(os.path.abspath(__file__)))  # 获取当前文件的文件夹的绝对路径
# print(os.path.dirname(CURRENT_DIR)) # 项目文件夹绝对路径
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(CURRENT_DIR)

# 添加项目至环境变量
sys.path.append(BASE_DIR)

from main import main  # 相当于把main和当前文件合并 所以执行的话也会执行main

if __name__ == '__main__':
    main.run()
