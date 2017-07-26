#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: rpc_server.py
# @time: 17/7/26 下午11:10

import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='rpc_queue')  # 声明用于接收客户端发送消息的queue


def fib(n):
    """
    :param n: fib的位数
    :return: 位数对应的值
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def on_request(ch, method, props, body):
    """
    接受客户端发送的消息
    """
    n = int(body)
    response = fib(n)
    # 处理消息返回给客户端
    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id=props.correlation_id),
                     body=str(response))
    # 发送消息处理完成回执
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)  # 同一时间最多处理一条
channel.basic_consume(on_request, queue='rpc_queue')  # 定义接受消息的回调和队列
print('[x] Await RPC requests')

channel.start_consuming()  # 开始接收消息

if __name__ == '__main__':
    pass
