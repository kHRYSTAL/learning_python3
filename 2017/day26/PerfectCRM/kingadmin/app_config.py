#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: app_config.py
# @time: 18/3/26 下午2:59

from django import conf

for app in conf.settings.INSTALLED_APPS:
    # 反射导入app.kingadmin从而找到表
    # print(__import__(app))
    try:
        print("import", __import__("%s.kingadmin" % app))
    except ImportError as e:
        print("app has no module kingadmin")
