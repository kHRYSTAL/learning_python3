### 协程与异步IO的区别

    多路复用中 epoll 在linux底层是通过 libevent.so实现的
    协程 gevent(遇到阻塞就切换其他函数)
    所以底层是一样的 但是关注点不一样epoll 关注的是阻塞时的切换
    gevent是更上层的封装 能够随便手动切换

### RabbitMQ 消息队列
    Python Queue
           threading Queue 不能跨进程通信
           multiprocess  Queue 用于父进程与子进程通信或同属于同一父进程下的子进程通信

    RabbitMQ 用于不同语言 不同应用程序(不同进程)间的通信 是一个中间代理
        也就是说 RabbitMQ本身是一个独立的进程 且内部维护的不止是一个队列
        rabbitMQ 依赖erlang 是通过erlang开发的 Windows需要安装这个语言


    在python中 推荐使用pika 实现RabbitMQ
        pika依赖RabbitMQ进行收发消息 需要先下载RabbitMQ 并启动

[安装](http://www.rabbitmq.com/install-standalone-mac.html)

[MAC 启动RabbitMQ](http://blog.csdn.net/u010046908/article/details/54773323)


        安装python rabbitMQ module

        pip install pika
        or
        easy_install pika
        or
        源码

        https://pypi.python.org/pypi/pika


![sample_p_c](http://images2015.cnblogs.com/blog/720333/201609/720333-20160923111427277-763273185.png)

    多消费者 单生产者模型
    在piko中 如果有多个消费者接受同一个管道的消息进行处理消费,
    消息采用轮询均衡的分配给多个消费者
    如消息A,B,C 会分别发给消费者1, 2, 3, 当消息D发送的时候 会发给消费者1

    # 消费消息
    channel.basic_consume(callback,  # 接收到消息的回调, 收到消息执行该函数
                          queue='hello',
                          # no_ack=True # 不需要确认 为 真 如果为假 需要手动确认
                          )
    # no_ack 默认为false 表示rabbitMQ需要确认callback是否执行完, 应该按照需求设置这个参数,
    # 如果为False 表示需要手动确认
    # 需要 在callback函数中增加ch.base_ack(delivery_tag=method.delivery_tag) 进行手动确认 否则rabbitMQ认为没有执行完或出现异常中断 新连接的消费者会继续收到这个消息
    # rabbitMQ会存储到内存(如果没有其他消费者)或交给这个管道的其他消费者(进程)去处理, 即使[重启消费者]也会接收到未处理完的callback等待处理
    # 如果为True 表示不需要确认 rabbitMQ 发送消息后 就不会管消息是否被正确处理 如果消费者处理出现中断 这个消息也不会被找回


    查看rabbitMQ 管道名称和消息数量  sbin/rabbitmqctl list_queues

    队列持久化:
        如果rabbitMQ 服务断掉 实际上队列就丢了(因为在内存中)
        需要在声明管道的时候 加上 durable=True 表示队列进行持久化存储
        channel.queue_declare(queue='hello', durable=True)

    消息持久化
        设置durable 为True 只是将队列进行持久化 实际上消息还是在内存中的
        如果需要将消息进行持久化 需要在发消息时加上 properties=pika.BasicProperties(delivery_mode=2)

        channel.basic_publish(exchange='',  #
                      routing_key='hello',  # 发送消息到哪个序列
                      body='Hello World!',  # 消息内容
                      properties=pika.BasicProperties(delivery_mode=2))  # 消息持久化存储

### Redis

### Mysql

