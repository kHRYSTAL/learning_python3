#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: publisher.py
# @time: 17/7/31 上午12:11


# noinspection PyUnresolvedReferences
from monitor import RedisHelper

obj = RedisHelper()
obj.public('hello')
