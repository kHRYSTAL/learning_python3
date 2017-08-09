#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 环境变量配置
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: fuck_it.py
# @time: 17/8/9 下午2:21
import os
import sys

# 项目路径
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

print(BASE_DIR)
# 添加至环境变量
sys.path.append(BASE_DIR)

if __name__ == '__main__':
    from modules import actions

    actions.excute_from_command_line(sys.argv)
