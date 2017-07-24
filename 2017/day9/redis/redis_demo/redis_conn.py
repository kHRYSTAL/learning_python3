#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: redis_conn.py
# @time: 17/7/24 下午10:45

import redis

r = redis.Redis(host='127.0.0.1', port=6379)  # 创建redis连接

r.set('foo', 'bar')
print(r.get('foo'))

