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


##### RabbitMQ fanout广播模式
        1. 当生产消息过多时
            RabbitMQ 消息是公平的分发的 但是机器配置有可能有高有低 因此需要负载均衡处理
            机器配置高的机器 处理的消息多, 配置低的机器 处理的消息少
            RabbitMQ 只需要简单的处理就可以"公平"的分发消息:
                检查处理消息的客户端 队列中还有多少条消息 如果消息数量大于1 则不发给客户端

                消费者(客户端)添加channel.basic_qos(prefetch_count=1) 加到consume之前
        2. 广播(群发消息)
           生产者生产一条消息 所有绑定相关转化器的消费者都能接收到
           如果需要这种效果, 就需要使用exchange参数了

           Exchange在定义的时候是有类型的，以决定到底是哪些Queue符合条件，可以接收消息


            fanout: 所有bind到此exchange的queue都可以接收消息
            direct: 通过routingKey和exchange决定的哪个queue可以接收消息
                    注:这里的routingKey可以认为是tag或级别
                       生产者将消息发送给exchange exchange按照routingKey 发送给相应的级别, 监听这个routingKey级别的消费者能够接收
            topic:所有符合routingKey(此时可以是一个表达式)的routingKey所bind的queue可以接收消息

            　　 表达式符号说明：#代表一个或多个字符，*代表任何字符
                  例：#.a会匹配a.a，aa.a，aaa.a等
                      *.a会匹配a.a，b.a，c.a等
                 注：使用RoutingKey为#，Exchange Type为topic的时候相当于使用fanout　
            headers: 通过headers 来决定把消息发给哪些queue

            ======注意: 广播群发消息======
            ======不管消费者是否消费收没收到,======
            ======广播消息是实时的======
            ======发完消息就不管了======

        fanout 方式 群发:

            生产者生产消息后 将消息发给转化器exchange 转化器去发送广播,
            消费者还是从queue去取消息 因此queue需要去绑定转化器
            消息流程
                生产者->转化器(遍历绑定的队列fanout群发)->绑定转化器的队列->消费者

            消费者:
                import pika

                connection = pika.BlockingConnection(pika.ConnectionParameters(
                    host='localhost'))
                channel = connection.channel()

                channel.exchange_declare(exchange='logs',
                                         type='fanout')
                # exclusive 排他的 唯一的
                result = channel.queue_declare(exclusive=True)  # 不指定queue名字,rabbit会随机分配一个名字,exclusive=True会在使用此queue的消费者断开后,自动将queue删除
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

![exchange_publisher_fanout](http://www.rabbitmq.com/img/tutorials/python-three-overall.png?_=5248247)

        direct 有指向性的发送:
                在queue中,
                生产者可以判断将消息发送到哪个级别的消费者
                消费者可以绑定接收那几个级别的消息
                也就是说 多个消费者可以按照级别选择接收同一个queue中的消息

![publisher-direct](http://www.rabbitmq.com/img/tutorials/python-four.png)

        topic: 更细致的指向性发送
            topic能够更细致的按照关键字去发送
            在相同转换器且是topic类型下
            消费者绑定的如果是'#' 则是接收所有消息


![publisher-topic](http://www.rabbitmq.com/img/tutorials/python-five.png?_=5248247)






### Redis

### Mysql

