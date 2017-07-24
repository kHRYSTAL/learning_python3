#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: fanout_publisher.py
# @time: 17/7/17 下午7:10

import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs',  # tag
                         type='fanout')  # 群发消息

message = ' '.join(sys.argv[1:]) or "info: Hello World!"  # 通过命令行调用, 后面输入要发送的消息
channel.basic_publish(exchange='logs',  # 将消息发送到名称为logs的转换器,
                      routing_key='',  # 广播不需要输入queue名称, 但是要写空
                      body=message)
print(" [x] Sent %r" % message)
connection.close()

if __name__ == '__main__':
    pass
