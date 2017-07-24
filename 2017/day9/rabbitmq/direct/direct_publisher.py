#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: direct-publisher.py
# @time: 17/7/17 下午11:53

import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs',
                         type='direct')

severity = sys.argv[1] if len(sys.argv) > 1 else 'info' # 命令行输入, 第一个参数指定级别 消费者用于判断是否接收
message = ' '.join(sys.argv[2:]) or 'Hello World!'
channel.basic_publish(exchange='direct_logs',   # 任意声明的转换器
                      routing_key=severity,  # routing_key指定的是级别, 不是管道, 消费者监听转换器就可以
                      body=message)
print(" [x] Sent %r:%r" % (severity, message))
connection.close()


if __name__ == '__main__':
    pass