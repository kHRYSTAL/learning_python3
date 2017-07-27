### RabbitMQ, Redis, MySQL

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


#### Rabbit MQ RPC

    remote procedure call 远程调用协议
    远程发送指令 另一端接收指令执行 执行完成后返回结果
    如SNMP 等等都是RPC

    在rabbitmq中 之前的使用方式都是一端(server)发送消息至queue,  另一端(client)去接收queue中的消息处理 但处理完成后没有返回结果
    通知发送消息的一端, 那么如何返回结果呢?

    建立两个mq, 一个用于server发送消息给client, 一个用于client发送结果给server

    [参考demo rpc]



### Redis 缓存系统

    用于应用/后台 对某些数据的存放和获取

    常用缓存系统
        mongodb  默认配置是存到内存也存到硬盘
        redis    默认配置是只存到内存(可配置持久化至硬盘) 效率更高速度更快
        memcache 轻量级缓存, 只能存到内存

##### 为什么使用Redis

    redis 是单线程的 使用epoll模式实现了高并发

[安装redis](https://jingyan.baidu.com/article/f3e34a12dfefddf5eb6535fe.html)

    默认端口6379
    启动redis-server:安装目录src下 启动redis-server
    启动redis-client:安装目录src下 启动redis-cli
#### redis string 操作
![](http://images2015.cnblogs.com/blog/720333/201612/720333-20161224160558276-436576532.png)
    语法:
        set [key] [value] 存储 键值对
        set name khrystal
        set name khrystal ex 2 存储键值对 只存活2秒钟
        -------
        get [key] 通过key获取value
        get name
        如果返回(nil) 表示为空
        -------
        keys * 列出所有key

###### 在python中使用redis
    import redis
    r = redis.Redis(host='127.0.0.1', port=6379)  # 创建redis连接
    r.set('foo', 'bar')
    print(r.get('foo'))

    每次set和get实际上都是一个socket连接, 为了避免频繁连接 释放开销
    可以使用连接池


#### Redis API使用
    redis-py 的API的使用可以分类为：

    连接方式
    连接池
    操作
    String 操作
    Hash 操作
    List 操作
    Set 操作
    Sort Set 操作
    管道
    发布订阅

### [api 参考](http://www.cnblogs.com/alex3714/articles/6217453.html)

  >  set(name, value, ex=None, px=None, nx=False, xx=False)

    在Redis中设置值，默认，不存在则创建，存在则修改
    参数：
         ex，过期时间（秒）
         px，过期时间（毫秒）
         nx，如果设置为True，则只有name不存在时，当前set操作才执行
         xx，如果设置为True，则只有name存在时，岗前set操作才执行
#### redis hash操作
![](http://images2015.cnblogs.com/blog/720333/201612/720333-20161224162531620-762875117.png)

    hset info name khrystal # 在info 中存放key-value
    hset info age 22
    hset info sex male

    HGETALL info # 获取数据
    HGET info name # 获取某个value
    HKEYS info # 获取info中的所有key
    HVALS info # 获取info 中所有value

    批量操作
    HMSET info name khrystal age 22 # 批量设置key-value
    HMGET info name age # 批量获取
    hlen info # 获取有几个key
    hexists info sex # 判断是否存在 0 不存在 1 存在
    hdel info name # 删除一个key


### [python中hash操作api](http://www.cnblogs.com/alex3714/articles/6217453.html)

#### redis list操作
![](http://images2015.cnblogs.com/blog/720333/201612/720333-20161224164119620-243246367.png)

    lpush names khrystal, matt, jack # 存放key - [value1, value2]
    lrange names 0 -1 # 获取第0个到倒数第一个, 就是取所有
                # 返回 jack, matt, khrystal 栈, 后进先出
    lpush 是从左向列表放置数据 RPUSH 是从右向列表放数据这lrange就能获取正序数据

    LINSERT names BEFORE matt haha # 向matt左边插入haha
    LINSERT names AFTER matt haha # 向matt右边插入haha
    LSET names 3 PAPA # 修改第三个位置为PAPA
    LREM names 1 PAPA # 从左侧删除 1个 value为PAPA的item
    LPOP names # 从左侧获取并删除这个数据
    LTRIM 1 3 # 只保留1-3index的数据 其他都移除
    RPOPLPUSH names names2 # 从names右侧获取数据并在names删除 从左侧设置到names2中
    BLPOP names 10 # 删除names中的第一个数据并获取 如果没有值等待10秒 在10秒中如果有值会删除
                   # 可以做类似生产者消费者模式
    BROPOLPUSH names names2 40 # 在40秒中 names中如果被设置了数据 会pop出,并设置到names2中
                                # 两个列表同步, 一边删除一边增加

#### redis set集合操作

    sadd name matt matt # 向集合中设置两个相同数据 实际上只有一个 因为去重了 这里集合是无序的
    SMEMBERS name # 获取name集合中的成员 无序
    sdiff name name2 # 获取name和name2的差集, 即name中存在 但name2中不存在的数据
    SDIFFSTORE name3 name name2 将name和name2的差集放到name3中
    SINTER name name2 # 获取name和name2的交集 即name中存在且在name2中也存在的数据
    SISMEMBER name matt # matt是否是name中的元素
    SRANDMEMBER name [n] # 从name中随机获取一个或多个值
    SREM name matt # 从name中删除matt
    SUNION name name2 # 获取name和name2的并集
    SUNION name4 name name2 # 将name和name2的并集放到name4
    sscan name4 0 match m* # 获取name4中 从第0个开始 m开头的元素


##### redis 有序集合

    zadd name 10 khrystal 5 matt 8 jack  # 在name中添加value的权重和value
    ZRANGE name 0 -1 # 获取集合中所有数据,此时是按照权重从小到大排列
    zadd name 4 khrystal # 因为是集合 此时会把khrystal的权重改为4
    ZRANGE name 0 -1 withscores 获取所有数据 包涵权重
    ZCARD name 获取name中元素的数量
    ZCOUNT name 6 12 # 获取name中权重在 6到12之间的value的个数
    ZRANK name matt # 获取matt在name中的排行 排行从0开始
    ZREM name matt  # 删除matt
    ZREMRANGEBYRANK name  0 2 # 删除排行从0到2的value
    ZSCORE name matt # 获取matt的权重
    ZINTERSTORE name3  2 name name2 # 获取两个(2的作用)有序集合的交集
                                   # 则会把权重相加放到name3

#### redis 其他常用操作

### Mysql

