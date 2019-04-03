#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: statistic_file_type_count.py
# @time: 19/3/19 下午6:22
import os
import sys

sys.setrecursionlimit(1000000)

# 主工程绝对路径 需要替换
ABS_ROOT_DIR_PATH = '/Users/kHRYSTAL/GithubProject/zhislandgit'

type_dict = {}


def statistic_file_type(path):
    files = os.listdir(path)
    for filename in files:
        temp_path = os.path.join(path, filename)
        if os.path.isdir(temp_path):
            # 递归
            statistic_file_type(temp_path)
        elif os.path.isfile(temp_path):
            # 获取后缀名
            type_name = os.path.splitext(temp_path)[1]
            # 无后缀名文件
            if not type_name:
                type_dict.setdefault("None", 0)
                type_dict["None"] += 1
            else:
                type_dict.setdefault(type_name, 0)
                type_dict[type_name] += 1


if __name__ == '__main__':
    statistic_file_type(ABS_ROOT_DIR_PATH)
    print("总文件数:[%d]" % (sum(type_dict.values())))
    for each_type in type_dict.keys():
        print("文件后缀[%s]--文件个数[%d]" % (each_type, type_dict[each_type]))
