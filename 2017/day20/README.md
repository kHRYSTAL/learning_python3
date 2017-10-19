##### 知识点概要

- Session
- CSRF
- Model操作
- Form验证(ModelForm)
- 中间件
- 缓存
- 信号


1. Session

        cookies优点是把存储的压力存储在客户端电脑上
        基于Cookies做用户验证时 不建议将敏感信息(用户名/密码) 存储为cookie
        因为cookie的特性 前端可以查看与修改 这样是非常不安全的
        因此 如果要做敏感信息存储 且不需要频繁查询数据库的话 应当使用Session



        1. 原理
            cookie是保存在用户浏览器端的键值对
            session是保存在服务器端的键值对
                那么 如何验证某个客户端对应服务器内的session?
                    实际上session还是依靠于cookie, 在浏览器客户端的cookie中
                    存储指向服务器session的唯一标识 当浏览器访问服务器时携带cookie
                    服务器通过cookie中的标识去获取这个用户的敏感信息
                    这样 就实现了session的获取与唯一

        2. 操作
            如果服务器需要处理session 一定要先执行以下两个命令
            python manage.py makemigrations
            python manage.py migrate

                django会将session生成的唯一标识存储于数据库中 表名为django_session
                而标识对应的数据也加密存储于这个表中 列名为session_data
                还有一列数据为失效日期



            def login(request):
                if request.method == 'GET':
                    return render(request, 'login.html')
                elif request.method == 'POST':
                    user = request.POST.get('user')
                    pwd = request.POST.get('pwd')
                    if user == 'root' and pwd == '123':
                        # 生成随机字符串
                        # 写到用户浏览器cookie
                        # 保存至session中 key为随机字符串 value为用户相关信息
                        # django 会自动执行以上所有操作 只需要一行代码
                        request.session['username'] = user
                        request.session['is_login'] = True
                        return redirect('/index/')
                    else:
                        print('用户名密码不正确')
                        return render(request, 'login.html')


            def index(request):
                # 获取session 实际操作时查询表django_session表中这个客户端的唯一标识的对象中is_login的值
                if request.session['is_login']: # 如果不存在则报错
                    return HttpResponse('Index OK')
                else:
                    return HttpResponse('滚')


        3. 实现两周内自动登录

            在Django中 Session默认的超时时间是2周
            即表中超时时间默认为2周 cookie设置默认也为2周
            可通过配置文件修改默认配置 参考[4.所有操作]

            - request.session.set_expiry(60 * 10) # 修改为超时时间为600秒
            - SESSION_SAVE_EVERY_REQUEST = True

        3.5. Django中Session的优势

            如果session的数据在服务器端只存在于数据库
            那么直接做数据库存储和获取不就完了吗? 实际上在Django中Session的处理不只局限于数据库
            1.默认情况下是在数据库存储的
                SESSION_ENGINE = 'django.contrib.sessions.backends.db'

            2.可修改为在缓存中存储
                SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
                # 使用的缓存别名（默认内存缓存，也可以是memcache），此处别名依赖缓存的设置
                SESSION_CACHE_ALIAS = 'asdf'
               如果使用缓存存储 需要指定cache连接位置 如:
               参考 settings.py
                 CACHES = {
                            'asdf': {
                                'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
                                'LOCATION': '127.0.0.1:11211',
                                'LOCATION': '192.168.2.1:11211',
                            }
                        }

            3. 可修改为文件存储
                 SESSION_ENGINE = 'django.contrib.sessions.backends.file'    # 引擎
                 # 缓存文件路径，如果为None，则使用tempfile模块获取一个临时地址tempfile.gettempdir()
                 # 如：/var/folders/d3/j9tj0gz93dg06bmwxmhh6_xm0000gn/T
                 SESSION_FILE_PATH = None

            4. 缓存+数据库 用于提高查询效率
                 # 相当于二级缓存 如果缓存中有直接取出 如果没有再去数据库查询
                 SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'

            5. 加密存储
                 SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'


        4. 所有操作

            Django默认支持Session，并且默认是将Session数据存储在数据库中，即：django_session 表中。

            a. 配置 settings.py

                数据库缓存配置

                    SESSION_ENGINE = 'django.contrib.sessions.backends.db'   # 引擎（默认）

                    SESSION_COOKIE_NAME ＝ "sessionid"                       # Session的cookie保存在浏览器上时的key，即：sessionid＝随机字符串（默认）
                    SESSION_COOKIE_PATH ＝ "/"                               # Session的cookie保存的路径（默认）
                    SESSION_COOKIE_DOMAIN = None                             # Session的cookie保存的域名（默认）
                    SESSION_COOKIE_SECURE = False                            # 是否Https传输cookie（默认）
                    SESSION_COOKIE_HTTPONLY = True                           # 是否Session的cookie只支持http传输（默认）
                    SESSION_COOKIE_AGE = 1209600                             # Session的cookie失效日期（2周）（默认）
                    SESSION_EXPIRE_AT_BROWSER_CLOSE = False                  # 是否关闭浏览器使得Session过期（默认）
                    SESSION_SAVE_EVERY_REQUEST = False                       # 是否每次请求都保存Session，默认修改之后才保存（默认）

                内存缓存配置

                    SESSION_ENGINE = 'django.contrib.sessions.backends.cache'  # 引擎
                    SESSION_CACHE_ALIAS = 'default'                            # 使用的缓存别名（默认内存缓存，也可以是memcache），此处别名依赖缓存的设置


                    SESSION_COOKIE_NAME ＝ "sessionid"                        # Session的cookie保存在浏览器上时的key，即：sessionid＝随机字符串
                    SESSION_COOKIE_PATH ＝ "/"                                # Session的cookie保存的路径
                    SESSION_COOKIE_DOMAIN = None                              # Session的cookie保存的域名
                    SESSION_COOKIE_SECURE = False                             # 是否Https传输cookie
                    SESSION_COOKIE_HTTPONLY = True                            # 是否Session的cookie只支持http传输
                    SESSION_COOKIE_AGE = 1209600                              # Session的cookie失效日期（2周）
                    SESSION_EXPIRE_AT_BROWSER_CLOSE = False                   # 是否关闭浏览器使得Session过期
                    SESSION_SAVE_EVERY_REQUEST = False                        # 是否每次请求都保存Session，默认修改之后才保存

                文件缓存配置
                    SESSION_ENGINE = 'django.contrib.sessions.backends.file'    # 引擎
                    SESSION_FILE_PATH = None                                    # 缓存文件路径，如果为None，则使用tempfile模块获取一个临时地址tempfile.gettempdir()                                                            # 如：/var/folders/d3/j9tj0gz93dg06bmwxmhh6_xm0000gn/T


                    SESSION_COOKIE_NAME ＝ "sessionid"                          # Session的cookie保存在浏览器上时的key，即：sessionid＝随机字符串
                    SESSION_COOKIE_PATH ＝ "/"                                  # Session的cookie保存的路径
                    SESSION_COOKIE_DOMAIN = None                                # Session的cookie保存的域名
                    SESSION_COOKIE_SECURE = False                               # 是否Https传输cookie
                    SESSION_COOKIE_HTTPONLY = True                              # 是否Session的cookie只支持http传输
                    SESSION_COOKIE_AGE = 1209600                                # Session的cookie失效日期（2周）
                    SESSION_EXPIRE_AT_BROWSER_CLOSE = False                     # 是否关闭浏览器使得Session过期
                    SESSION_SAVE_EVERY_REQUEST = False                          # 是否每次请求都保存Session，默认修改之后才保存

            b. 使用

                def index(request):
                    # 获取、设置、删除Session中数据
                    request.session['k1'] # 如果不存在则报错
                    request.session.get('k1',None)
                    request.session['k1'] = 123
                    request.session.setdefault('k1',123) # 存在则不设置
                    del request.session['k1'] # 删除当前用户session中的k1

                    # 所有 键、值、键值对
                    request.session.keys()
                    request.session.values()
                    request.session.items()
                    request.session.iterkeys()
                    request.session.itervalues()
                    request.session.iteritems()


                    # 用户session的随机字符串
                    request.session.session_key

                    #  重要 将所有Session失效日期小于当前日期的数据删除
                    request.session.clear_expired()

                    # 检查 用户session的随机字符串 在数据库中是否
                    request.session.exists("session_key")

                    # 删除当前用户的所有Session数据 参数为唯一标识 常用于注销登出操作
                    request.session.delete(request.session.session_key)
                    request.session.clear()

                    request.session.set_expiry(value)
                        * 如果value是个整数，session会在些秒数后失效。
                        * 如果value是个datatime或timedelta，session就会在这个时间后失效。
                        * 如果value是0,用户关闭浏览器session就会失效。
                        * 如果value是None,session会依赖全局session失效策略。


2. CSRF

    * CSRF 原理

            防止跨站请求伪造原理 第一次请求时(GET) 会返回数据和一个加密的字符串 这个加密字符串只有自己能反解
            下次请求(POST)的时候 需要携带这个字符串 如果字符串不正确 则会返回403forbidden
            在settings.py中, 中间件'django.middleware.csrf.CsrfViewMiddleware' 就是做了一层防止CSRF的防护
            在post提交时 需要携带csrf_token 经过CsrfViewMiddleware 的校验 才能到达Views中
            Django会自动将这段随机字符串放到cookie(key: csrftoken)中, 供表单提交和ajax提交使用

    * 无CSRF时存在的隐患

            XSS攻击 脚本注入后拿走当前用户的cookie 通过你的cookie去登录
            CSRF就是防止跨站请求伪造

    * Form 提交(CSRF)

            html获取显示: {{ csrf_token }}
                    表单中使用 csrf_token: {% csrf_token %}
                      会自动生成一个隐藏的input标签:
                      <input type="hidden" name="csrfmiddlewaretoken" value="7wvtmpp6PNnKSFqCa2344wAmUCwLBoYLZyM4zzRURe33KAI8XM4hSQP0oL2P1o4M">

    * Ajax 提交 (CSRF) CSRF请求头 X-CSRFToken

             <script>
                $(function () {
                    var csrftoken = $.cookie('csrftoken');
                    $('#btn').click(function () {
                       $.ajax({
                           url:'/login/',
                           type:'POST',
                           data: {'user': 'root', 'pwd': '123'},
                           headers: {'x-csrftoken': csrftoken},
                           success: function (arg) {
                                window.location.href = '/index/'
                           }

                       });
                    });
                });
             </script>

             也可以进行通用配置设置CSRF, 该页面的所有ajax请求都会先执行这个函数
                  function csrfSafeMethod(method) {
                        // 这些 HTTP methods 不会设置csrftoken
                        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
                  }
                  // 通用配置设置 所有ajax请求都会先执行这个函数
                  $.ajaxSetup({
                        beforeSend: function (xhr, settings) {
                         // 如果提交方式不是GET等请求 且没设置csrfdomain
                         if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                             xhr.setRequestHeader('X-CSRFtoken', $.cookie('csrftoken'))
                         }
                        }
                  });
    * 注意

             只要使用django.middleware.csrf.CsrfViewMiddleware这个全局配置
             所有post请求都需要加csrftoken, 这样是明显不合适的
             因此可以使用局部装饰器配置
                全局：

                　　中间件 django.middleware.csrf.CsrfViewMiddleware

                局部：

                @csrf_protect，为当前函数强制设置防跨站请求伪造功能，即便settings中没有设置全局中间件。
                @csrf_exempt，取消当前函数防跨站请求伪造功能，即便settings中设置了全局中间件。
                注：from django.views.decorators.csrf import csrf_exempt,csrf_protect

3. 中间件(MiddleWare)

        客户端请求至服务器views前 服务器的中间件能够拦截到客户端的请求 进行处理
        在settings.py中 Django默认提供了一些中间件
        我们也可以自定义中间件 实现 process_request方法即可

        class RowOne(MiddlewareMixin):
            def process_request(self, request):
                print("RowOne MiddleWare")

        request中间件流向按照settings中Middleware列表的顺序执行

        同时也可以拦截响应 实现 process_response方法即可
            def process_response(self, request, response):
                print("RowOne MiddleWare response")
                return response

        response中间件流向按照Middleware列表的逆序执行


        拦截请求示例:
             def process_request(self, request):
                if request.method == 'POST':
                    if int(request.POST.get('money', 0)) == 0:
                        return HttpResponse('滚')

             中间件可以实现黑名单过滤 或者 校验操作 日志操作等等

        process_view: 拦截 view处理 正序执行

            def process_view(self, request, view_func, view_func_args, view_func_kwargs):
                print("RowOne Middleware process view")

                参数:
                    view_func views中请求对应的函数
                    view_func_args 函数的可变长度参数
                    view_func_kwargs 函数的关键字参数

        process_exception : 拦截 异常处理 逆序执行 如果被处理 不会再向上执行 直接抛给逆序的process_response

            def process_exception(self, request, exception):
                print("RowOne MiddleWare handle exception")


        process_template_response: views中的函数返回的对象中具有render方法 会触发这个函数
                即Middleware如果检索到对象内部包含函数名为render 就会触发这个函数 参考 views.py#Foo

            def process_template_response(self, request, response):
                # 这个函数会自动将对象的response从render函数中解析出来
                print("RowOne Middle handle template response")

        拦截流程 process_request -> process_view -> views -> (process_exception) -> process_template_response -> process_response
            如果views抛出异常 且 中间件进行了异常拦截 则会进行中间件异常处理

4. 缓存

        只有Django支持缓存功能

        Django中提供了6种缓存方式：

            开发调试
            内存
            文件
            数据库
            Memcache缓存（python-memcached模块）
            Memcache缓存（pylibmc模块）

    a. 开发调试

            # 此为开始调试用，实际内部不做任何操作
            # 配置：
                CACHES = {
                    'default': {
                        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',     # 引擎
                        'TIMEOUT': 300,                                               # 缓存超时时间（默认300，None表示永不过期，0表示立即过期）
                        'OPTIONS':{
                            'MAX_ENTRIES': 300,                                       # 最大缓存个数（默认300）
                            'CULL_FREQUENCY': 3,                                      # 缓存到达最大个数之后，剔除缓存个数的比例，即：1/CULL_FREQUENCY（默认3）
                        },
                        'KEY_PREFIX': '',                                             # 缓存key的前缀（默认空）
                        'VERSION': 1,                                                 # 缓存key的版本（默认1）
                        'KEY_FUNCTION' 函数名                                          # 生成key的函数（默认函数会生成为：【前缀:版本:key】）
                    }
                }


            # 自定义key
            def default_key_func(key, key_prefix, version):
                """
                Default function to generate keys.

                Constructs the key used by all other methods. By default it prepends
                the `key_prefix'. KEY_FUNCTION can be used to specify an alternate
                function with custom key making behavior.
                """
                return '%s:%s:%s' % (key_prefix, version, key)

            def get_key_func(key_func):
                """
                Function to decide which key function to use.

                Defaults to ``default_key_func``.
                """
                if key_func is not None:
                    if callable(key_func):
                        return key_func
                    else:
                        return import_string(key_func)
                return default_key_func

    b. 内存

            # 此缓存将内容保存至内存的变量中
            # 配置：
                CACHES = {
                    'default': {
                        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
                        'LOCATION': 'unique-snowflake',
                    }
                }

            # 注：其他配置同开发调试版本

    c. 文件

            # 此缓存将内容保存至文件
            # 配置：

                CACHES = {
                    'default': {
                        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
                        'LOCATION': '/var/tmp/django_cache',
                    }
                }
            # 注：其他配置同开发调试版本

    d. 数据库

            # 此缓存将内容保存至数据库
            # 配置：
                CACHES = {
                    'default': {
                        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
                        'LOCATION': 'my_cache_table', # 数据库表
                    }
                }

            # 注：执行创建表命令 python manage.py createcachetable

    e. Memcache缓存（python-memcached模块）

            # 此缓存使用python-memcached模块连接memcache
            CACHES = {
                'default': {
                    'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
                    'LOCATION': '127.0.0.1:11211',
                }
            }

            CACHES = {
                'default': {
                    'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
                    'LOCATION': 'unix:/tmp/memcached.sock',
                }
            }

            CACHES = {
                'default': {
                    'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
                    'LOCATION': [
                        '172.19.26.240:11211',
                        '172.19.26.242:11211',
                    ]
                }
            }

    f. Memcache缓存（pylibmc模块）

            # 此缓存使用pylibmc模块连接memcache
            CACHES = {
                'default': {
                    'BACKEND': 'django.core.cache.backends.memcached.PyLibMCCache',
                    'LOCATION': '127.0.0.1:11211',
                }
            }

            CACHES = {
                'default': {
                    'BACKEND': 'django.core.cache.backends.memcached.PyLibMCCache',
                    'LOCATION': '/tmp/memcached.sock',
                }
            }

            CACHES = {
                'default': {
                    'BACKEND': 'django.core.cache.backends.memcached.PyLibMCCache',
                    'LOCATION': [
                        '172.19.26.240:11211',
                        '172.19.26.242:11211',
                    ]
                }
            }

    使用缓存功能:

           Django提供了三个级别的缓存存储

           1. 针对单独的views函数进行缓存, 针对整个页面级别的缓存

                方式一：
                    from django.views.decorators.cache import cache_page

                    @cache_page(60 * 15)
                    def my_view(request):
                        ...

                方式二：
                    from django.views.decorators.cache import cache_page

                    urlpatterns = [
                        url(r'^foo/([0-9]{1,2})/$', cache_page(60 * 15)(my_view)),
                    ]

           2. 针对页面局部标签缓存

                a. 引入TemplateTag

                    {% load cache %}

                b. 使用缓存 单位为秒

                    {% cache 5000 缓存key %}
                        缓存内容
                    {% endcache %}

           3. 全站使用缓存(使用中间件)

                 使用中间件，经过一系列的认证等操作，如果内容在缓存中存在，则使用FetchFromCacheMiddleware获取内容并返回给用户 不经过views
                 因此应把 FetchFromCacheMiddleware 写到最后
                 ，当返回给用户之前，判断缓存中是否已经存在，如果不存在则UpdateCacheMiddleware会将缓存保存至缓存 response之前的最后一个middleware，
                 因此应把 UpdateCacheMiddleware 写到最前
                 从而实现全站缓存

                    MIDDLEWARE = [
                        'django.middleware.cache.UpdateCacheMiddleware',
                        # 其他中间件...
                        'django.middleware.cache.FetchFromCacheMiddleware',
                    ]

                    CACHE_MIDDLEWARE_ALIAS = ""
                    CACHE_MIDDLEWARE_SECONDS = ""
                    CACHE_MIDDLEWARE_KEY_PREFIX = ""

           缓存的优先级:

                根据生命周期 全站缓存>views缓存>标签缓存
                因为标签缓存在view函数内部执行 view函数在中间件内部执行
                所以设置缓存根据生命周期UpdateCacheMiddleware最后执行
                获取缓存FetchFromCacheMiddleware最后执行


5. 信号

        def signal(request):
            """ 需求: 在每次save时记录数据库操作日志 """
            from app01 import models
            # 1
            obj = models.UserInfo(user='root')
            # 2
            # 3
            obj.save()
            # 4

            obj = models.UserInfo(user='root')
            obj.save()

            obj = models.UserInfo(user='root')
            obj.save()

        在Django中 余留了一些钩子用于通知外部创建了对象, 保存了数据库等操作
        (钩子余留位置如上方函数数字所示)
        在编写代码时 可以设置接受这些信号(钩子)的函数 进行记录操作或其他处理
        因此不需要重写save函数 不需要修改Django本身封装的一些数据库操作api

    Django中提供了“信号调度”，用于在框架执行操作时解耦。通俗来讲，就是一些动作发生的时候，信号允许特定的发送者去提醒一些接受者。

        Model signals
            pre_init                    # django的modal执行其构造方法前，自动触发
            post_init                   # django的modal执行其构造方法后，自动触发
            pre_save                    # django的modal对象保存前，自动触发
            post_save                   # django的modal对象保存后，自动触发
            pre_delete                  # django的modal对象删除前，自动触发
            post_delete                 # django的modal对象删除后，自动触发
            m2m_changed                 # django的modal中使用m2m字段操作第三张表（add,remove,clear）前后，自动触发
            class_prepared              # 程序启动时，检测已注册的app中modal类，对于每一个类，自动触发
        Management signals
            pre_migrate                 # 执行migrate命令前，自动触发
            post_migrate                # 执行migrate命令后，自动触发
        Request/response signals
            request_started             # 请求到来前，自动触发
            request_finished            # 请求结束后，自动触发
            got_request_exception       # 请求异常后，自动触发
        Test signals
            setting_changed             # 使用test测试修改配置文件时，自动触发
            template_rendered           # 使用test测试渲染模板时，自动触发
        Database Wrappers
            connection_created          # 创建数据库连接时，自动触发

    注册接受信号函数

        应同pymysql相同 在项目启动时就应该注册, 因此写到项目的__init__.py中

        1. 注册方式一: connect

            from django.db.models.signals import pre_init

            # 接受信号函数
            def callback(sender, **kwargs):
                print("pre_init_callback")
                print(sender, kwargs)

            # 注册接受数据库对象构造函数触发信号
            pre_init.connect(callback)

            参考__init__.py

        2. 注册方式二: 装饰器receiver

            from django.core.signals import request_finished
            from django.dispatch import receiver

            @receiver(request_finished)
            def my_callback(sender, **kwargs):
                print("Request finished!")

    自定义信号

        自定义信号不同于Django提供的内置信号 给开发者提供了更多扩展空间
        如监控内存 流量等等到达某一个状态 可以发送信号通知 可以用于监控

        a. 定义信号

            import django.dispatch
            pizza_done = django.dispatch.Signal(providing_args=["toppings", "size"])

        b. 注册信号

            def callback(sender, **kwargs):
                print("callback")
                print(sender,kwargs)

            pizza_done.connect(callback)

        c. 触发信号:
            由于内置信号的触发者已经集成到Django中，所以其会自动调用，
            而对于自定义信号则需要开发者在任意位置触发

            from 路径 import pizza_done
            pizza_done.send(sender='seven',toppings=123, size=456)

            参考views.custom_signal

6. 表单验证(ModelForm):

        使用Django的Form组件 在表单验证时避免写复杂的正则表达式进行校验

        可以利用Form创建一系列的规则 使接受到的表单数据与规则进行匹配

        views:
            class MyForm(forms.Form):
                """ 指定客户端发送的表单提取的字段 表单的name必须与变量名相同"""
                # 错误信息提示
                user = forms.CharField(error_messages={'required': '用户名不能为空'})
                pwd = forms.CharField(
                    max_length=12,
                    min_length=6,
                    error_messages={'required': '密码不能为空', 'min_length': '密码长度不能小于6', 'max_length': '密码长度不能大于12'}
                )
                email = forms.EmailField(error_messages={'required': '邮箱不能为空', 'invalid': '邮箱格式错误'})

            from app01 import models
            def test_form(request):
                if request.method == 'GET':
                    # GET 请求 只提供表单 内部会进行require 和 长度 格式的处理
                    form = MyForm()
                    return render(request, "form_test.html", {'form': form})
                elif request.method == 'POST':
                    # 获取用户所有的数据
                    form = MyForm(request.POST)
                    # 每条数据请求的验证是否通过 res为boolean
                    res = form.is_valid()
                    print(res)
                    if res:
                        # 验证成功 获取所有的正确信息
                        # {'user': 'assa', 'pwd': 'sadasd', 'email': 'sdasdsad@123.com'}
                        print(form.cleaned_data)
                        models.UserInfo.objects.create(**form.cleaned_data)
                        return HttpResponse("注册成功")
                    else:
                        # 验证失败 显示错误信息
                        return render(request, "form_test.html", {'form': form})
                    return redirect('/test_form/')


        html:

            <form action="{{request.path_info}}" method="post">
                {% csrf_token %}
                <!-- 可自动生成标签 且自动提示错误信息 但定制化困难 -->
                <!--{{ form.as_p }}-->
                <!--{{ form.as_ul }}-->
                <!--<table>-->
                    <!--{{ form.as_table }}-->
                <!--</table>-->

                 <!--定制化生成标签-->
                <p>{{ form.user }} {{ form.errors.user.0 }}</p>
                <p>{{ form.pwd }} {{ form.errors.pwd.0 }}</p>
                <p>{{ form.email }} {{ form.errors.email.0 }}</p>
                <input type="submit" value="提交"/><br/>
            </form>










