#### socket

> 所有的网络协议本质上都是对数据的收发

socket封装了tcp, udp
暴露给外部的只有收发动作
所有的协议基本都是基于socket的, 区别只是收发交互方式和数据类型的不同

1. 简易的cs结构

2. 通过cs结构实现简易ssh效果

3. ftp server

        读取文件名
        检测文件是否存在
        打开文件
        检测文件大小
        把文件大小发送给客户端
        等待客户端确认
        开始边读边发数据
        发送md5给客户端
        关闭文件
4. socketserver: 处理多个请求

        First, you must create a request handler处理类 class by subclassing the BaseRequestHandler class and overriding覆盖 its handle() method; this method will process incoming requests. 　　
        你必须自己创建一个请求处理类，并且这个类要继承BaseRequestHandler,并且还有重写父亲类里的handle()
        Second, you must instantiate实例化 one of the server classes, passing it the server’s address and the request handler class.
        你必须实例化TCPServer ，并且传递server ip 和 你上面创建的请求处理类 给这个TCPServer
        Then call the handle_request() or serve_forever() method of the server object to process one or many requests.
        server.handle_request() #只处理一个请求
        server.serve_forever() #处理多个请求，永远执行
        Finally, call server_close() to close the socket.

        ThreadingTCPServer: 每一个请求就会开启一个线程
        ForkingTCPServer: 每一个请求就会开启一个进程(windows系统下没有fork, 所以在windows上无效)


allow_reuse_address:允许重用地址

    断开后重新运行有时会出现'address already in use'错误
    需要等待几十秒 如果不想等待 可以使用该参数
    在普通socket上:
        server = socket.socket()
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    在socketserver上:
        self.allow_reuse_address
