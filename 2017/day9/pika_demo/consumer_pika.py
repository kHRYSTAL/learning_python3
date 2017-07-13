#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: consumer_pika.py
# @time: 17/7/12 下午11:13


import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
    'localhost'))
channel = connection.channel()

# You may ask why we declare the queue again ‒ we have already declared it in our previous code.
# We could avoid that if we were sure that the queue already exists. For example if send.py program
# was run before. But we're not yet sure which program to run first. In such cases it's a good
# practice to repeat declaring the queue in both programs.
# 因为在同一台机器中 无法肯定生产者先执行还是消费者先执行 如果不加这句话 消费者先执行 queue管道实际上还不存在 会直接报错
channel.queue_declare(queue='hello', durable=True)  # durable 持久化存储

"""
consumer_callback(channel, method, properties, body)
                channel: BlockingChannel
                method: spec.Basic.Deliver
                properties: spec.BasicProperties
                body: str or unicode
"""


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    ch.base_ack(delivery_tag=method.delivery_tag)  # 告知rabbitMQ 消息被正确处理


# 消费消息
channel.basic_consume(callback,  # 接收到消息的回调, 收到消息执行该函数
                      queue='hello',
                      # no_ack=True
                      )
# no_ack 默认为false 表示rabbitMQ需要确认callback是否执行完, 应该按照需求设置这个参数,
# 如果为False 表示需要手动确认
# 需要 在callback函数中增加ch.base_ack(delivery_tag=method.delivery_tag) 进行手动确认 否则rabbitMQ认为没有执行完或出现异常中断 新连接的消费者会继续收到这个消息
# rabbitMQ会存储(没有其他消费者)或交给这个管道的其他消费者(进程)去处理, 即使重启也会接收到未处理完的callback等待处理
# 如果为True 表示不需要确认 rabbitMQ 发送消息后 就不会管消息是否被正确处理 如果消费者处理出现中断 这个消息也不会被找回

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()  # 等待消费接收到的消息
