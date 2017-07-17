#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: fanout_subscriber.py
# @time: 17/7/17 下午7:13

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'))
channel = connection.channel()

# 声明接收转化器的名称和类型
channel.exchange_declare(exchange='logs',  # 接收名称为logs的转换器的消息
                         type='fanout')
# exclusive 排他的 唯一的
result = channel.queue_declare(exclusive=True)  # 不指定queue名字,rabbit会随机分配一个名字,exclusive=True会在使用此queue的消费者断开后,自动将queue删除, 这个queue是消费者与转换器之间的
queue_name = result.method.queue  # 获取随机生成的队列名称

channel.queue_bind(exchange='logs',  # 绑定这个生产者的tag(转化器/exchange)
                   queue=queue_name)

print(' [*] Waiting for logs. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] %r" % body)


channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()

if __name__ == '__main__':
    pass
