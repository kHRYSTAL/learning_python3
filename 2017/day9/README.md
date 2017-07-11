### 协程与异步IO的区别

    多路复用中 epoll 在linux底层是通过 libevent.so实现的
    协程 gevent(遇到阻塞就切换其他函数)
    所以底层是一样的 但是关注点不一样epoll 关注的是阻塞时的切换
    gevent是更上层的封装 能够随便手动切换

### RabbitMQ 消息队列
    Python Queue
           threading Queue 不能跨进程通信
           multiprocess  Queue 用于父进程与子进程通信或同属于同一父进程下的子进程通信
    RabbitMQ 用于不同语言 不同应用程序(不同进程)间的通信

### Redis

### Mysql

