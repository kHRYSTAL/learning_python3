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

