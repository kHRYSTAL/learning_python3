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

### Redis

### Mysql

