#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: pika使用RabbitMQ 发送消息 可以跨进程 跨机器发送或接收消息
#           这个文件是一个生产者
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: producer_pika.py
# @time: 17/7/12 下午11:05

import pika
"""
在pika中 连接(connection的概念被淡化)
管道的概念加重 发送消息接受消息都使用管道
"""

# 创建一个socket连接
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
# 在这个socket中创建一个管道
channel = connection.channel()
# 在管道中创建一个叫hello的队列
channel.queue_declare(queue='hello', durable=True)

# RabbitMQ a message can never be sent directly to the queue, it always needs to go through an exchange.
# 向管道中发送消息
channel.basic_publish(exchange='',  #
                      routing_key='hello',  # 发送消息到哪个序列
                      body='Hello World!',  # 消息内容
                      properties=pika.BasicProperties(delivery_mode=2))  # 消息持久化存储
print(" [x] Sent 'Hello World!'")
connection.close()

if __name__ == '__main__':
    pass
