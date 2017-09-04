### 补充以及后续路线
    1. js正则
        test    用于判断字符串是否符合规定的正则表达式, 只要内部含有就返回true
        exec    获取匹配的数据

        1. 创建正则表达式对象 需要使用/.../ 不需要加""
            如 匹配数字的正则:
                var reg = /^\d+$/; \d+表示字符串为全为数字 需要加开始和终止 否则只要包含就返回true
               判断
                reg.test("asdfg12"); 返回值为false

        2. 获取匹配数据
            var str = asdf_12_asdf_34;
            var reg = /\d+/;
            reg.exec(str) 由于惰性 所以只返回[12] 拿不到34

            2.1 分组 二级匹配
            var str = "JavaScript is more fun than Java or JavaBeans";
            var reg = /\bJava(\w+)\b/; ()表示分组, \b表示字母
            此时进行匹配, 会先进行整体匹配, 由于惰性, 只获取JavaScript, 然后再从匹配到的字符串中再获取括号中的内容
            结果为
            [JavaScript, Script]

            2.2 全局匹配
                在正则表达式尾部加g为全局匹配 非惰性:
                var str = "JavaScript is more fun than Java or JavaBeans";
                var reg = /\bJava\w+\b/g;
                // exec为迭代器匹配
                reg.exec(str); ["JavaScript"]
                reg.exec(str); ["Java"]
                reg.exec(str); ["JavaBeans"]
                reg.exec(str); null
                reg.exec(str); 重新一轮匹配, ["JavaScript"]

            2.3 分组+全局匹配
                var str = "JavaScript is more fun than Java or JavaBeans";
                var reg = /\bJava(\w+)\b/g;
                // exec为迭代器匹配
                reg.exec(str); ["JavaScript", "Script"]
                reg.exec(str); ["Java", ""]
                reg.exec(str); ["JavaBeans", "Beans"]
                reg.exec(str); null
                reg.exec(str); 重新一轮匹配, ["JavaScript", "Script"]

            2.4 其他
                /.../i 不区分大小写
                /.../m 多行匹配 注意 js正则本身默认就是多行匹配
                        加上m后 是为了解决有^存在的正则 同时字符串是多行, 检测多行的开头 而不是字符串的开头
                        如:
                        var str = "JavaScript is more fun than \nJava or JavaBeans"
                        var reg = /^Java(\w+)/g;
                        reg.exec(str); ["JavaScript", "Script"]
                        reg.exec(str);  null 此时返回为空 因为只会匹配这个str字符串整体开头为Java的部分
                                            后面都不会匹配 因为不是开头

                        解决方式
                        var str = "JavaScript is more fun than \nJava or JavaBeans"
                        var reg = /^Java(\w+)/mg;

                        reg.exec(str); ["JavaScript", "Script"]
                        reg.exec(str); ["Java", ""]
                        reg.exec(str); null 因为只匹配行的开头 不会匹配JavaBeans 因为不是行的开头

    1.1 登录注册验证

        <form>
            <input type="text"/>
            <input type="password"/>
            <input type="submit"/>
        </form>

        $(":submit").click(function(){
            boolean flag = true
            $(":text, :password").each(function(){

                if(...){
                    // 如果输入不合法 不允许href跳转 return false
                    flag = flase;
                    return false; // 终止循环
                }
            });

            return flag;
        });

        默认事件(href..) 与自定义事件(onclick..)的执行顺序
            参考s1.html
        默认事件先执行的标签
            <input type="password"/>
            <input type="checkbox"/>
        自定义事件先执行
            <a/>
            <input type="submit"/>


        注意: 在前端做表单验证是不完善的, 因为浏览器的js可以被禁用




    2. 组件
        面临选择
            1. 所有页面自己实现重头开发
                优点 写完了能够知道全部实现
                缺点 重复造轮子

            2. 实现已经封装好的ui组件
                常用:BootStrap 包含css, js的封装 ui好看 能够做后台管理 web主站ui
                    jQueryUI 包含css, js的封装 功能丰富 但ui不好看 偏向做后台管理系统
                    EasyUI  css js 需要ajax操作 改起来比较麻烦 偏向做后台管理系统

                都需要学习组件实现的规则

    3. web框架
        自己实现一个简易的web框架

    4. Django
        python实现web网站功能最齐全(orm, web, 模版等)的框架

### 学习BootStrap规则

    1.响应式布局 bootstrap大量存在@media用于响应式布局
        页面的自适应 会设置一个条件
            如最小宽度 当页面最小宽度没有达到条件时 某些style不生效
        页面样式会跟随浏览器大小修改而改变
            使用@media
        参考s2.html

    2.图标

    3.基本使用
        1. 导入 修改属性
        参考s3.html


### 例子
    1. 使用bxslider 实现轮播
        参考s4.html


### Django

    1. socket后台
        所有的服务器后台实际上都是基于socket 接收一个客户端socket请求, 返回数据后断开
        参考s1.py

    2.WSGI Web Server Gateway Interface 是一种规范 定义了使用python编写web app 与web server之间的接口
        格式, 实现web app与web server之间的解藕

        python标准库提供的独立WSGI服务器称为wsgiref. 是基于socket的封装
        参考s2.py

        wsgi本身是一套接口规则 用于实现socket
        以下模块均实现了wsgi 本质上就是为了创建socket
            server_names = {
                'cgi': CGIServer,
                'flup': FlupFCGIServer,
                'wsgiref': WSGIRefServer,
                'waitress': WaitressServer,
                'cherrypy': CherryPyServer,
                'paste': PasteServer,
                'fapws3': FapwsServer,
                'tornado': TornadoServer,
                'gae': AppEngineServer,
                'twisted': TwistedServer,
                'diesel': DieselServer,
                'meinheld': MeinheldServer,
                'gunicorn': GunicornServer,
                'eventlet': EventletServer,
                'gevent': GeventServer,
                'geventSocketIO':GeventSocketIOServer,
                'rocket': RocketServer,
                'bjoern' : BjoernServer,
                'auto': AutoServer,
            }

    3. Web框架
        1.MVC
            Model - 数据层操作 基本为耗时操作 如查询数据库 查询远程服务器数据等
            View - 视图层 用户可见ui 模版文件
            Controler - 控制MV 业务处理
        2.MTV (实际上就是改个名)
            Model - 数据层
            Templeate 模版文件
            View - 业务处理


        Django实际上就是个MTV框架
            Model为数据层处理
            Template为模版文件(ui)
            View为业务处理

    4. Django 命令 创建程序
        1. 配置环境变量
        2. 切换到指定目录 执行django-admin startproject [项目名称] 创建项目

               自动生成的项目结构为
               mysite
                    mysite          # 对整个程序进行配置的文件夹
                        __init__.py
                        settings.py # 配置文件
                        urls.py     # url对应关系 (path与函数的映射)
                        wsgi.py     # 遵循wsgi规范, 默认使用uwsgi 配合nginx就是个完整的服务器了
                    manage.py       # 管理django程序
                                        - python manage.py
                                        - python manage.py startapp
                                        - python manage.py manemigrations
                                        - python manage.py migrate
                    templates       # html模版存放路径 可自定义
                    static          # 静态文件存放路径 css, js

        3. 命令行执行 python manage.py runserver [127.0.0.1:8001] 启动服务器
        4. 浏览器打开127.0.0.1:8001
            显示Django运行成功

        5. 创建应用 python manage.py startapp [appname]
        6. 填写逻辑代码至views测试

        注: django 是自动更新的 不需要手动重新启动

        project app下目录结构

        app:
            - migrations        # 数据库操作记录(修改表结构的记录)
                与sqlarchemy不同 django支持修改表结构
            - admin.py          # Django为开发者提供的后台管理系统
                 参考 mysite
            - apps.py           # 配置当前app的文件
            - models.py         # 创建数据库表结构的文件 ORM工具 通过命令就可以创建修改数据库结构
            - tests.py          # 单元测试使用
            - views.py          # 用于写当前app的业务逻辑代码





#### 创建数据库表结构:
    1.在app的models中写好表结构 并在project settings中添加app后
        执行 python manage.py makemigrations(更新表结构) 即可创建表 默认使用自带的sqlite3
    2.在app的admin中注册后台管理可以看到的表
        如:
            admin.site.register(models.UserInfo)
            admin.site.register(models.UserType)
        并创建后台管理系统root用户, 使用命令:
            python manage.py migrate 同步数据库
            python manage.py createsuperuser 创建project 后台root用户

            输入用户名密码邮箱后即创建完成
            执行python manage.py runserver 127.0.0.1:8001
            在http://127.0.0.1:8001/admin/即可看到管理系统

        注意: 每次更新表结构都需要执行
                python manage.py makemigrations
                python manage.py migrate


        在项目开发中 mysite就是一个完整的项目 而myapp相当于业务中的一个模块,
            你可以把所有模块都写到一个app中 但是为了分层 不同的业务应写到不同的app中




### views 操作

    1. render(递交给客户端)
        def login(request):
            # f = open('template/login.html', 'r', encoding='utf-8')
            # data = f.read()
            # f.close()
            # return HttpResponse(data)
            # 上述代码可以使用render一行解决
            return render(request, 'login.html')

        为什么没有template? 可以在project的settings.py下配置模版文件路径

### 配置模版路径
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [os.path.join(BASE_DIR, 'templates')],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ]

    在views中使用:
        def login(request):
            # 使用render一行解决 去模版文件夹寻找模版文件
            return render(request, 'login.html')


### 配置静态文件路径
    # 静态文件前缀 在template中使用的静态文件都会通过前缀去找寻STATICFILES_DIRS下的文件
    STATIC_URL = '/static/'

    # 配置静态文件目录路径
    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, 'static'),
    )

    在html中使用:
        <link rel="stylesheet" href="/static/commons.css">












