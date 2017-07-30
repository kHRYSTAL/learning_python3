#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: monitor.py
# @time: 17/7/31 上午12:08

import redis


class RedisHelper:
    def __init__(self):
        self.__conn = redis.Redis(host='10.211.55.4')
        self.chan_sub = 'fm104.5'
        self.chan_pub = 'fm104.5'

    def public(self, msg):
        self.__conn.publish(self.chan_pub, msg)  # 向channel中发送消息
        return True

    def subscribe(self):
        pub = self.__conn.pubsub()  # 开始订阅, 相当于打开收音机
        pub.subscribe(self.chan_sub)  # 订阅的channel
        pub.parse_response()  # 准备接收, 再次调用为真正接收
        return pub
