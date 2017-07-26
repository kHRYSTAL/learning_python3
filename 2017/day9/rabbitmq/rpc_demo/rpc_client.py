#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: rpc_client.py
# @time: 17/7/26 下午10:49

import pika
import uuid


class FibonacciRpcClient(object):
    def __init__(self):
        """
        声明接受服务端的消息的队列
        """
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        self.channel = self.connection.channel()  # 获取channel
        result = self.channel.queue_declare(exclusive=True)  # 声明一个随机队列
        self.callback_queue = result.method.queue  # 获取这个队列
        # 定义消费回调函数和监听队列
        self.channel.basic_consume(self.on_response, no_ack=True, queue=self.callback_queue)

    def on_response(self, ch, method, props, body):
        """
        接受服务端发送的消息
        这里的参数都是basic_consume必须有的
        :param ch:
        :param method:
        :param props:
        :param body:
        :return:
        """
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self, n):
        """
        向服务端发送消息
        :param n:
        :return:
        """
        self.response = None
        self.corr_id = str(uuid.uuid4())  # 生成一个随机id代表消息的id 用于判断接收的消息是否是针对这个发送消息的回复
        self.channel.basic_publish(exchange='',
                                   routing_key='rpc_queue',
                                   properties=pika.BasicProperties(  # 基本配置
                                       reply_to=self.callback_queue,  # 告诉服务端回复的队列名称
                                       correlation_id=self.corr_id,  # 告诉服务端回复的队列id
                                   ),
                                   body=str(n))  # 发送的消息
        while self.response is None:
            """
            注意:start_consume是阻塞的, 为了保持客户端不阻塞 应使用下方代码 持续执行while循环
            """
            self.connection.process_data_events()  # 非阻塞的start_consume() 等待接收服务端的消息
        return int(self.response)  # 当服务端的消息接收到, 返回服务端的消息


fibonacci_rpc = FibonacciRpcClient()
print('[x] Request fib(30')
response = fibonacci_rpc.call(30)
print('[.] Got %r' % response)

if __name__ == '__main__':
    pass
