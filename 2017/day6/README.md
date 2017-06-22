##进程线程协程


### paramiko

    Paramiko模块

    paramiko主要用于远程ssh连接服务器进行批量管理操作

    SSH 有scp命令可以传文件 scp是基于ssh的sftp协议

    `scp -rp -P22 temp.txt root@10.0.0.41:/tmp/` r为如果是目录拷贝目录 p为permission拷贝权限至远程机器

    top, vim 不能返回, top -bn


#### ssh 密钥
> 不通过明文用户名密码 使用RSA非对称密钥加密 自动连接远程机器

公钥 public key
私钥 private key
A: 10.0.0.31(持有A私钥) ---> B: 10.0.0.41 (持有A公钥)

生成密钥对命令 `ssh -keygen`


### 线程
> 操作系统调度cpu执行运算的指令的集合

线程 == 一堆指令

线程是操作系统最小的调度单位 是一串指令的集合

线程被包涵在进程之中, 是进程的实际运作单位


### 进程
> 应用程序以一个整体的形式暴露给操作管理, 里面包含对各种资源的调用,
内存的管理, 网络接口的调用等..
对各种资源管理的集合就可以成为进程


进程要操作CPU, 必须通过线程

> 问题:进程启动快还是线程启动快?

    线程快 因为线程是cpu指令集 进程需要先开辟资源空间 再启动线程

同进程的线程共享内存空间 进程间的内存空间是独立的

    父进程创建两个子进程 子进程的数据相当与父进程的拷贝 是独立的且不能互相访问
    同一个进程内的线程可以互相访问进程的数据涉及到数据的共享与信息的传递

    如果两个进程想通信 需要一个中间代理去实现

    新的线程可以简单的创建 新的进程对其父进程进行一次克隆(耗费内存)

    一个线程可以控制和操作同一进程里的其他线程, 但是进程只能操作子进程

    对于主线程的修改 有可能会影响到其他线程的行为(运行)(主线程结束,守护线程会中断)
    对于父进程的修改(不是删除) 不会影响子进程


线程实现方式

    1.方法调用
    def run(n):
        """
        task
        """
        print('task', n)
        time.sleep(2)


    # target 参数为执行的目标函数, args 为参数 类型为元组
    t1 = threading.Thread(target=run, args=('t1',))
    t2 = threading.Thread(target=run, args=('t2',))

    t1.start()
    t2.start()

    2.类的继承, 参照文件


线程的join()函数 如果线程没有执行完, 会在join()函数等待

线程执行完成之后才会向下继续执行 可以进行线程控制操作和顺序执行

    start_time = time.time()
    t_objs = []  # 将数据添加到列表里,用于循环执行完执行join()
    for i in range(20):
        t = MyThread(('i=%s' % i))
        t.start()
        t_objs.append(t)

    for t in t_objs:
        t.join()
    print('cost time:', time.time() - start_time)


守护进程(线程) setDeamon(True)

    线程可以设置主从关系
    如果不加join 线程实际是并行的没有主从关系
        (实际上主线程还是等所有线程都执行完才退出程序, 说明最后有一个join())
    如果设置了其他线程为守护线程 ,如果主线程执行完毕 就会直接退出程序
            守护线程也会退出 不再执行 因为守护线程是'从' 程序不会管它是否结束

    start_time = time.time()
    t_objs = []  # 将数据添加到列表里,用于循环执行完执行join()
    for i in range(20):
        t = MyThread(('i=%s' % i))
        t.setDaemon(True) # 一定要在start之前设置
        t.start()
        t_objs.append(t)
    print('cost time:', time.time() - start_time)
    # 执行到这里程序退出 不会管t的操作是否完成
    print('main thread:', threading.current_thread())


GIL 全局解释器锁:

    单核多线程执行
    虽然单核可以通过CPU频繁切换上下文线程看起来像并行的
    但单核肯定是串行的 而不是并行的


    但是在python中 无论有多少核
        [同一时间 执行的线程只有一个! 这是cpython的设计缺陷]
        python的线程是假线程

    这个就叫全局解释器锁, python的线程调用的是操作系统的原生线程pthread,
        java是自己实现的线程

    python 为了解决多个线程操作同一资源的同步问题
        从解释器出口控制 同一时间 只有一个线程能够工作, 其他线程只能干等着
        如 4核4个线程对一个int数据递增 ,启动线程 通过python-os-cpu(execute thread)
        4个线程在4个核上, 通过GIL 但是同一时间只有一个thread在执行
        所以cpython 不需要关系synchorized问题

    cpython 有全局解释器锁 GIL
    pypy 没有GIL 支持即时编译 JIT(预编译)


互斥锁(锁) :(仅适用于2.x, 3.x做了优化 不需要加锁) 保证多个线程操作同一个数据时 数据的唯一性

    import time
    import threading

    def addNum():
        global num #在每个线程中都获取这个全局变量
        print('--get num:',num )
        time.sleep(1)
        lock.acquire() #修改数据前加锁
        num  -=1 #对此公共变量进行-1操作
        lock.release() #修改后释放

    num = 100  #设定一个共享变量
    thread_list = []

    lock = threading.Lock() #生成全局锁

    for i in range(100):
        t = threading.Thread(target=addNum)
        t.start()
        thread_list.append(t)

    for t in thread_list: #等待所有线程执行完毕
        t.join()

    print('final num:', num )


在python2.x上 cpu每执行100条指令(解释器指令) 释放GIL, 切换一次线程
切换线程时 会将当前上下文存放在cpu寄存器中 下次切换回线程 会从寄存器取上次存放的数据

因此有可能会导致数据错乱

![GIL](http://images2015.cnblogs.com/blog/720333/201609/720333-20160909174150473-664853910.png)

死锁的解决:

    使用RLock 递归锁

信号量(semaphore)

    互斥锁 同时只允许一个线程更改数据, 而信号量可以允许一定数量的线程更改数据
    如厕所有3个坑 那最多只允许3个人上厕所(线程) 后面的人只能等里面有人出来才能进
    (Java 线程池)


事件(Events)

    事件是简单的同步对象 用于线程之间的数据同步
    事件可被所有线程查看或修改 实际上事件就是线程之间共享的资源
    通过事件的修改 可以对多个线程进行不同的控制

    红绿灯(线程) 车辆(线程) (改变红绿灯)event

    红绿灯线程通过改变红绿灯 车辆进行轮询检测event状态 如果是红灯就停止 绿灯就执行

    event = threading.Event()
    event.wait() # 等待被设定 如果没有设置 会阻塞 (红灯)不向下执行
    event.set() # 设置event 绿灯 wait()就不会阻塞
    event.clear() # 清空 再次等待被设定 会阻塞(红灯)
    event.is_set() # 判断是否设置标志

队列(Queen)

    queue.Queue(maxsize=0) # 先进先出 FIFO
    queue.LifoQueue(maxsize=0) # 后进先出 LIFO
    queue.ProiorityQueue(maxsize=0) # 存储数据时可设置优先级(VIP先出)

    可以调用q.get_nowait()
    如果没有数据会抛出异常
    或者判断q.qsize()

    """
    参数block 为True就是没数据时阻塞, time 为超时时间
    Queue.get(block=True, timeout=None)
    """
    # 可以设置队列最大容量
    # q = queue.Queue(maxsize=3)
    # 如果队列满了 再put会阻塞

    # todo
    Queue.task_done()