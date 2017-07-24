#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: redis_conn_pool.py
# @time: 17/7/24 下午11:11

import redis

pool = redis.ConnectionPool(host='127.0.0.1', port='6379')

r = redis.Redis(connection_pool=pool)
r.set('foo', 'bar')
print(r.get('foo'))