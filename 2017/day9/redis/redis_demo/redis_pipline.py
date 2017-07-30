#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: redis_pipline.py
# @time: 17/7/30 下午11:57


import redis

pool = redis.ConnectionPool(host='localhost', port=6379)

r = redis.Redis(connection_pool=pool)

# pipe = r.pipeline(transaction=False)
pipe = r.pipeline(transaction=True)

pipe.set('name', 'alex')  # 设置执行命令
pipe.set('role', 'sb')

pipe.execute()  # 执行事务
