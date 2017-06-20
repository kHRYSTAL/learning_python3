##进程线程协程


### paramiko

    数据库操作与Paramiko模块

    paramiko主要用于远程ssh连接服务器进行批量管理操作

    SSH 有scp命令可以传文件 scp是基于ssh的sftp协议

    `scp -rp -P22 temp.txt root@10.0.0.41:/tmp/` r为如果是目录拷贝目录 p为permission拷贝权限至远程机器

    top, vim 不能返回, top -bn


#### ssh 密钥
> 不通过明文用户名密码 使用RSA非对称密钥加密 自动连接远程机器

公钥 public key
私钥 private key
A: 10.0.0.31(持有A公钥) ---> B: 10.0.0.41 (持有A私钥)

生成密钥对 `ssh -keygen`


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

进程启动快还是线程启动快?

    线程快 因为线程是cpu指令集 进程需要先开辟空间 再启动线程

线程共享内存空间 进程的内存是独立的

    父进程创建两个子进程 子进程的数据相当与父进程的拷贝 是独立的且不能互相访问
    同一个进程内的线程可以互相访问进程的数据涉及到数据的共享与信息的传递

    如果两个进程想通信 需要一个中间代理去实现

    新的线程可以简单的创建 新的进程对其父进程进行一次克隆(耗费内存)

    一个线程可以控制和操作同一进程里的其他线程, 但是进程只能操作子进程

    对于主线程的修改 有可能会影响到其他线程的行为(运行)
    对于父进程的修改(不是删除) 不会影响子进程


线程实现方式

    1.方法调用
    def run(n):
    """
    task
    """
    print('task', n)
    time.sleep(2)


    # target 参数为执行的目标函数, args 为参数 元组
    t1 = threading.Thread(target=run, args=('t1',))
    t2 = threading.Thread(target=run, args=('t2',))

    t1.start()
    t2.start()

    2.类的继承


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





