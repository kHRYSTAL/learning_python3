> io操作不占用CPU

由于python一个进程在cpu上不管有多少核是实际单线程执行的, 多线程实际上只是在CPU上频繁的进行上下文切换

造成的假象, 因此python不适合cpu密集操作型任务(多线程图形计算运算 频繁cpu指令)!!

适合io操作密集型的任务(socketserver数据传输, cpu运算少)

如果python一定要进行cpu密集型操作, 可以使用多进程(多进程不能相互访问)

因为多进程就可以有多线程同时执行, 多进程可以解决多核问题

可以折中的解决cpu密集型操作的缺陷

### 多进程(multiprocessing)

    def thread_run():
    print(threading.get_ident())


    def f(name, num):
        time.sleep(2)
        print('hello ', name, num)
        # 在进程中启动线程
        t = threading.Thread(target=thread_run)
        t.start()


    if __name__ == '__main__':
        for i in range(10):
            p = multiprocessing.Process(target=f, args=('bob', i))
            p.start()
            # p.join()

### 进程间通讯

    不同进程间内存是不共享的 要想实现两个进程间的数据交换 可以用以下方法

    Queues 队列(数据的传递)
    使用方法跟threading里的queue差不多


    Pipes 管道(原理是socket)(数据的传递)
    Socket 套接字

    Managers 共享内存(数据的共享 可修改同一份数据)

       A manager returned by Manager() will support types list,
       dict, Namespace, Lock, RLock, Semaphore,
       BoundedSemaphore, Condition, Event, Barrier,
       Queue, Value and Array.

       Manager, 用于在进程中共享的对象 可以是字典 锁 列表等等
       每个进程都可以对这个对象进行操作

       Manager 默认是加锁的, 不需要再加锁

       Manager的原理是每个进程拷贝了相同的数据 然后覆盖到一个共有的加锁的内存中的对象上

    [进程之间的共享数据是通过pickle序列化实现的
      说白了就是两个进程操作同一个数据, 数据是一份(序列化的对象) 但两个进程间的内存对象(反序列化数据)是两份]
      需要注意两个进程同时修改同一份数据的问题

### 进程锁

    子进程需要获取锁的实例(一个序列化的锁)

    进程之间的资源都是独立的,且共享的数据修改可以用manager解决
    为什么还要加锁??
        答:为了防止print争抢屏幕 比如每个进程都有print 输出到屏幕上
            有可能print一半 就被其他进程抢占屏幕 导致输出混乱

### 进程池 Pool


    apply(func, args) 每个串行执行 顺序的

    apply_async(func,args, [callback]) 每个异步并发执行  从进程池中取出一个进程执行func，args为func的参数
        它将返回一个AsyncResult的对象，你可以对该对象调用get()方法以获得结果。
        callback参数 等待进程执行完 会执行callback函数 callback函数是在主进程执行的 不是子进程!!


    close()  进程池不再创建新的进程

    join()   !!!wait进程池中的全部进程。必须对Pool先调用close()方法才能join。

    from multiprocessing import Process, Pool
    import time
    import os


    def Foo(i):
        time.sleep(2)
        print(i + 100)
        return i + 100


    def Bar(arg):
        print('-->exec done:', arg, os.getpid())


    pool = Pool(processes=5)

    for i in range(10):
        # pool.apply_async(func=Foo, args=(i,), callback=Bar)  # 并发执行, callback 执行进程为主进程
        pool.apply(func=Foo, args=(i,))  # 串行执行

    print('end')
    pool.close()  # 进程池不再接收新的进程
    pool.join()  # 进程池中进程执行完毕后再关闭，如果注释，那么程序直接关闭。

