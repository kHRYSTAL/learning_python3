### 协程

    协程，又称微线程，纤程。英文名Coroutine。一句话说明什么是线程：协程是一种用户态的轻量级线程。

    协程拥有自己的[寄存器上下文和栈](CPU只知道线程 线程的上下文和栈在CPU的寄存器上, 并不知道协程)。协程调度切换时，将寄存器上下文和栈保存到其他地方，在切回来的时候，恢复先前保存的寄存器上下文和栈。因此：

    协程能保留上一次调用时的状态（即所有局部状态的一个特定组合），每次过程重入时，就相当于进入上一次调用的状态，换种说法：进入上一次离开时所处逻辑流的位置。

    简而言之 就是如果一个函数使用协程 可以随时的跳出函数执行其他, 然后再跳入函数
    从而实现在单线程上执行类似多线程的并行操作

    协程的好处：

        无需线程上下文切换的开销
        无需原子操作锁定及同步的开销
        　　"原子操作(atomic operation)是不需要synchronized"，所谓原子操作是指不会被线程调度机制打断的操作；这种操作一旦开始，就一直运行到结束，中间不会有任何 context switch （切换到另一个线程）。原子操作可以是一个步骤，也可以是多个操作步骤，但是其顺序是不可以被打乱，或者切割掉只执行部分。视作整体是原子性的核心。
        方便切换控制流，简化编程模型
        高并发+高扩展性+低成本：一个CPU支持上万的协程都不是问题。所以很适合用于高并发处理。

    缺点：

        无法利用多核资源：协程的本质是个单线程,它不能同时将 单个CPU 的多个核用上,协程需要和进程配合才能运行在多CPU上.当然我们日常所编写的绝大部分应用都没有这个必要，除非是cpu密集型应用。
        进行阻塞（Blocking）操作（如IO时）会阻塞掉整个程序

### 异步IO（asyncio）

    在一个线程中，CPU执行代码的速度极快，然而，一旦遇到IO操作，如读写文件、发送网络数据时，就需要等待IO操作完成，才能继续进行下一步操作。这种情况称为同步IO。
    在IO操作的过程中，当前线程被挂起，而其他需要CPU执行的代码就无法被当前线程执行了。
    因为一个IO操作就阻塞了当前线程，导致其他代码无法执行，所以我们必须使用多线程或者多进程来并发执行代码，为多个用户服务。每个用户都会分配一个线程，如果遇到IO导致线程被挂起，其他用户的线程不受影响。
    多线程和多进程的模型虽然解决了并发问题，但是系统不能无上限地增加线程。由于系统切换线程的开销也很大，所以，一旦线程数量过多，CPU的时间就花在线程切换上了，真正运行代码的时间就少了，结果导致性能严重下降。
    由于我们要解决的问题是CPU高速执行能力和IO设备的龟速严重不匹配，多线程和多进程只是解决这一问题的一种方法。
    另一种解决IO问题的方法是异步IO。当代码需要执行一个耗时的IO操作时，它只发出IO指令，并不等待IO结果，然后就去执行其他代码了。一段时间后，当IO返回结果时，再通知CPU进行处理。

    在Android中 所有的io操作都是同步的 所以需要开辟线程
    也就是说,python的协程遇到耗时操作(io操作)就跳出函数 执行其他函数 等待io结果返回在执行
    而Android中没有协程的概念 只能开辟线程 等待回调结果


### greenlet 已经封装好的协程库 不需要再去写yield

    为什么是green? 协程又叫greenthread 即线程无切换开销 无阻塞 无需锁
    greenlet 封装了yield 手动切换生成器更方便

### gevent 基于greenlet封装 不需要再去手动切换

    import gevent
    import time


    def foo():
        print('Running in foo')
        gevent.sleep(2)  # 模拟io A
        print('Explicit 精确的 context switch to foo again')


    def bar():
        print('Explicit context to bar')
        gevent.sleep(1)  # 模拟io B
        print('Implicit context switch back to bar')


    """
    spawn 发起

    按列表顺序遍历执行生成器, 遇到sleep就切换函数, 如果遍历后重新执行, 函数还在sleep, 继续按顺序切换
    foo 遇到A 执行bar 遇到B  执行foo A还在执行 切换到foo B执行完了 执行bar后面代码
    执行foo

    相比串行执行(3秒) 代码执行io就跳转 实际上只执行了2秒
    """
    start_time = time.time()
    gevent.joinall([
        gevent.spawn(foo),
        gevent.spawn(bar)
    ])

    print(time.time() - start_time)  # 2s左右


### monkey 给程序中所有的io操作做上标记 用于让gevent进行协程操作

    from urllib import request
    import gevent
    from gevent import monkey
    import time

    """
    经过log判断 实际还是串行的, urllib进行io操作时,
    gevent 检测不到进行了io操作 因此不会遇到阻塞跳转,需要给urllib打monkey补丁
    """

    # 把当前程序的所有io操作单独做上标记
    monkey.patch_all()

    """
    在这里 相当于读取urllib内部的io操作做上标记
    """


    def f(url):
        print('GET: %s' % url)
        resp = request.urlopen(url)
        data = resp.read()
        # file = open('url.html', 'wb')
        # file.write(data)
        # file.close()
        print('%d bytes received from %s.' % (len(data), url))


    # f('http://www.jianshu.com/p/ebac88cdf9d6')
    # 串行爬取网页
    urls = ['http://www.python.org',
            'http://www.jianshu.com/p/ebac88cdf9d6',
            'http://github.com']

    start_time = time.time()
    for url in urls:
        f(url)

    print("串行", time.time() - start_time)  # 6秒


    # 协程爬取网页
    start_time = time.time()
    gevent.joinall([
        gevent.spawn(f, 'http://www.python.org'),
        gevent.spawn(f, 'http://www.jianshu.com/p/ebac88cdf9d6'),
        gevent.spawn(f, 'http://github.com')
    ])
    print("协程:", time.time() - start_time)  # 2秒




### gevent 实现单线程多并发socket

    def handle_request(conn):
    print('start_handle_request')
    while True:
        print('start_recv')
        data = conn.recv(1024)
        print('end_recv')
        if not data:
            print('client is lost')
            break
        print(type(data))
        print('server receive:', data.decode(encoding='utf-8'))
        conn.send(data)


    # 单个server 实现多连接
    server = socket.socket()
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # 绑定地址和端口
    server.bind(('localhost', 6869))
    # 监听
    server.listen()
    # 等待客户端消息
    print('start server success')

    while True:
        # 此处可以理解成阻塞, 等待消息
        # 实际上也是非阻塞的
        print('server_accept')
        conn, addr = server.accept()  # 第一次while循环 没有其他生成器可以切换 卡在switch, 第二次阻塞时已经生成了一个generator, 会switch到handle_request
        print('has_accept')
        """
        由于下方函数加入了gevent 则是协程式函数, 相当于g = generator, next(g) 则继续while循环
        server继续等待accept(), 每新来一个连接 都会新增一个生成器

        使用monkey使单线程上接收消息不阻塞, 即 遇到阻塞就switch到其他生成器
        可以理解成, 如果有两个连接, 就有两个handle_request生成器
        在遇到阻塞时 两个生成器内部频繁在阻塞位置切换(其实是事件驱动模型回调结果, cpu调度处理io后回调给gevent), 等待其中一个生成器不阻塞时 继续向下执行
        遇到阻塞 再挂起频繁切换
        """
        spawn = gevent.spawn(handle_request, conn)  # 此处代码并不执行, 而是等待while循环accept阻塞的switch
        print('generate a generator add to main thread')  # gevent生成一个协程函数, 等待switch时被调用

    简而言之
    用了gevent.monkey.patch_all(), 一遇到io阻塞就switch到gevent.spawn包裹的函数, 而gevent.spawn包裹的函数遇到阻塞, 会跳转至其他正在阻塞的位置检查,
    如果此时其他位置不阻塞了 会继续向下执行 直到遇到阻塞(再次switch)或执行完

    io执行完了cpu.epoll的回调, 会通过gevent再还原回协程阻塞的位置继续向下执行

### 事件驱动模型

     假设一个 UI界面 每次点击都有一个事件, 事件其实是存在于一个快速轮询的列表里
    当系统检测到列表有这个事件 回调相应的结果或函数 如onClick()、onKeyDown()等

    （1）每收到一个请求，创建一个新的进程，来处理该请求；
    （2）每收到一个请求，创建一个新的线程，来处理该请求；
    （3）每收到一个请求，放入一个事件列表，让主进程通过非阻塞I/O方式来处理请求

        上面的几种方式，各有千秋，
        第（1）中方法，由于创建新的进程的开销比较大，所以，会导致服务器性能比较差,但实现比较简单。
        第（2）种方式，由于要涉及到线程的同步，有可能会面临死锁等问题。
        第（3）种方式，在写应用程序代码时，逻辑比前面两种都复杂。
        综合考虑各方面因素，一般普遍认为第（3）种方式是大多数网络服务器采用的方式


    事件驱动编程是一种编程范式，这里程序的[执行流]由[外部事件](点击, 滑动, 事件发射)来决定。
    它的特点是包含一个[事件循环](轮询序列)，当外部事件发生时使用回调机制来触发相应的处理。另外两种常见的编程范式是（单线程）同步以及多线程编程。

### 三种方式花费的时间
![event-drive-model](http://www.aosabook.org/images/twisted/threading_models.png?_=5248247)


### IO模型

    所有的IO 最终结果都是执行完成后存在于kernel 其他进程从kernel去进行拷贝
    fd 文件描述符 IO操作的指令字符串(read, block, recvfrom) 通过文件描述符进程能够进行相关的操作


    1. 同步阻塞 遇到阻塞等待IO操作完成才能继续

    2. 同步非阻塞 遇到阻塞 返回error 通过判断是否是error(当不是error 执行拷贝和后续逻辑) 同时可以执行其他流程 (发送一个socket)
        也就是说 向kernel发送指令并不需要等待 这里是非阻塞的
        而从kernel拷贝数据到进程 实际上还是阻塞的

    3. I/O多路复用 multiplexing model 实际上还是同步IO 或者说是多个同步阻塞IO

        多路IO其实与同步阻塞原理相同(也就是说也会卡住) 但是select() 能够同时传递多个socket句柄给kernel

        select poll epoll (event driven IO) (发送多个socket)
        select/poll 好处在于单个process就可以同时处理多个网络连接IO

        当用户进程调用了select 那么整个进程就会block 同时kernel会监视所有select负责的socket, 当任何一个socket数据准备好了 select就会返回
        这时用户进程再调用连接server, select会返回活动socket, 服务端可read操作 将数据从kernel拷贝到当前进程(拷贝过程是阻塞的)

        所以 IO多路复用的特点就是通过一种机制 一个进程能同时等待多个fd(文件描述符)(单线程)
        而这些 其中任意一个进入读就绪状态 select()函数就可以返回

    4. 异步IO (asynchronous IO)

        用户进程发起read操作之后，立刻就可以开始去做其它的事。
        而另一方面，从kernel的角度，当它收到一个asynchronous read (指令)之后，
        首先它会立刻返回，[所以不会对用户进程产生任何block]。
        然后，[kernel会等待数据准备完成，然后将数据拷贝到用户内存]
        (与其他模型不同的是 数据的准备和拷贝都是内核解决的 而不是进程, 由于kernel进行拷贝 因此这步也是非阻塞的)，
        当这一切都完成之后，kernel会给用户进程发送一个signal，告诉它read操作完成了。

        也就是说不会阻塞 read操作后 进程会拿到一个票据 当kernel完成操作之后 返回结果 进程通过结果进行后续操作

    5. 信号驱动IO



    blocking和non-blocking的区别

    调用blocking IO会一直block住对应的进程直到操作完成，而non-blocking IO在kernel还准备数据的情况下会立刻返回。

    synchronous IO和asynchronous IO的区别

    在说明synchronous IO和asynchronous IO的区别之前，需要先给出两者的定义。POSIX的定义是这样子的：
    - A synchronous I/O operation causes the requesting process to be blocked until that I/O operation completes;
    - An asynchronous I/O operation does not cause the requesting process to be blocked;

    两者的区别就在于synchronous IO做”IO operation”的时候会将process阻塞。按照这个定义，之前所述的blocking IO，non-blocking IO，IO multiplexing都属于synchronous IO。

    有人会说，non-blocking IO并没有被block啊。这里有个非常“狡猾”的地方，定义中所指的”IO operation”是指真实的IO操作，就是例子中的recvfrom这个system call。non-blocking IO在执行recvfrom这个system call的时候，如果kernel的数据没有准备好，这时候不会block进程。但是，当kernel中数据准备好的时候，recvfrom会将数据从kernel拷贝到用户内存中，这个时候进程是被block了，在这段时间内，进程是被block的。

    而asynchronous IO则不一样，当进程发起IO 操作之后，就直接返回再也不理睬了，直到kernel发送一个信号，告诉进程说IO完成。在这整个过程中，进程完全没有被block。

![几种IO模型区别](http://images2015.cnblogs.com/blog/720333/201609/720333-20160916171648430-240094129.png)


#### 多路复用中的函数
> 每个链接大概消耗4k

* select 用于检测多个socket链接状态 在多路复用IO模型中使用

    最多只能维护1024个socket (linux默认文件最多打开数1024)

    当kernel 返回其中一个socket结果 select需要去循环遍历socket找到结果

* poll

    与select相同 但去掉了1024的限制

* epoll

    (nginx Django 等使用) centOS6后支持 windows不支持(只支持select)
    当socket有结果 kernel会告诉epoll 哪个socket有结果 去掉了遍历的时间消耗

    水平触发
        当用户(进程) 在收到kernel通知 由于忙碌没取数据, 数据存在kernel里
        除非用户主动调用read(socket调用receive) 下一次kernel还会再通知
    边缘触发
        kernel不会再通知 数据相当于取不回来了

    epoll的最大优点:
        1.没有最大数限制
            早期apache 没有使用epoll 3000个访问就瘫痪 nginx 10万个也没问题
        2.时间损耗少

    epoll是最常用的 内核对于异步IO支持不是很好 实现也比较复杂 (kernel需要自己去检测socket结果
        和拷贝结果到用户态)
    所谓的nginx 等框架 说是异步IO 实际上是使用epoll的多路复用


> 在python中 asyncio是真正的异步IO










