#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 导入包
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: package_main.py
# @time: 17/6/1 下午1:59
import package_test
from package_test import package_module as module

print(package_test.name)

module.say_hello()


if __name__ == '__main__':
    pass