#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: custom_exception.py
# @time: 17/6/8 下午5:22


class CustomException(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


try:
    raise CustomException('this is msg')
except CustomException as e:
    print(e)
else:
    print('not raise Exception')
finally:
    print('in the end run this')
