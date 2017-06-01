#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: from module import * 与 import的区别
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: main1.py
# @time: 17/6/1 上午11:29

"""
from module import * 没有模块前缀 等于把模块函数覆盖到当前代码文件中
如果出现重复变量或函数名 会按照先后顺序覆盖
"""
from module_sample import *


def logger():
    print('in the main1')


# from module_sample import *

logger()

if __name__ == '__main__':
    pass
