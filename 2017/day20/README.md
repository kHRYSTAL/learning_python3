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





