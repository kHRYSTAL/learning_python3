#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 导入模块并设置别名
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: main.py
# @time: 17/6/1 上午11:19
import module_sample as module


def logger():
    print('in the main')


print(module.module_name)
module.test()


logger()
module.logger()

if __name__ == '__main__':
    pass
