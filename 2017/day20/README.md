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
            - request.session.set_expiry(60 * 10)
            - SESSION_SAVE_EVERY_REQUEST = True


        4. 所有操作

            Django默认支持Session，并且默认是将Session数据存储在数据库中，即：django_session 表中。

            a. 配置 settings.py

                基本配置

                    SESSION_ENGINE = 'django.contrib.sessions.backends.db'   # 引擎（默认）

                    SESSION_COOKIE_NAME ＝ "sessionid"                       # Session的cookie保存在浏览器上时的key，即：sessionid＝随机字符串（默认）
                    SESSION_COOKIE_PATH ＝ "/"                               # Session的cookie保存的路径（默认）
                    SESSION_COOKIE_DOMAIN = None                             # Session的cookie保存的域名（默认）
                    SESSION_COOKIE_SECURE = False                            # 是否Https传输cookie（默认）
                    SESSION_COOKIE_HTTPONLY = True                           # 是否Session的cookie只支持http传输（默认）
                    SESSION_COOKIE_AGE = 1209600                             # Session的cookie失效日期（2周）（默认）
                    SESSION_EXPIRE_AT_BROWSER_CLOSE = False                  # 是否关闭浏览器使得Session过期（默认）
                    SESSION_SAVE_EVERY_REQUEST = False                       # 是否每次请求都保存Session，默认修改之后才保存（默认）

                缓存配置

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

