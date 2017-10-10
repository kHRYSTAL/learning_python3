##### 知识概要

* 路由系统 url映射
    1. 固定url 与 func 或 class.as_view()对应
    2. 正则表达式, 设置接受参数名称(?P<nid>\d+)
    3. 设置别名 name="xxx" 模版中通过 {% url "xxx" %} 获取url
       获取当前页面url {{ request.path_info }}
    4. 命名空间 app中添加urls.py, project设置根路径 include("app.urls")

        注意 支持多个前缀对应同一个py文件
        如 admin/app, crm/app
        可以对应同一个app.urls
        url(r'^admin/', include("app.urls"))
        url(r'^crm/', include("app.urls"))
        这样就导致了多个url指向同一个函数 可以使用 命名空间去区分到底是哪个url触发了函数
        include("app.urls", namespace='admin-name' )
        include("app.urls", namespace='crm-name' )

    5. 默认值 可以在url映射中填写默认值 如url(r'^root/', views.root, {'web': 'root'}),
       在views.python中需要增加形參去接收这个默认值 def root(request, web)

    6. 通过别名获取url reverse()

            project.url.py:
                url(r'^a/', include("app01.urls", namespace='crm-name' ))
            app01.url.py:
                url(r^(?P<pk>\d+)/$, views.detail, name='detail')
            app01.views.py:
                v = reverse('crm-name:detail', kwargs={'pk':123,}) 获取url为 a/123
            html
                {% url 'crm-name:detail' pk=123 %}

* Views
    - 请求的其他信息: 请求头

        服务端接受请求时 实际上接受的参数为 environ, 表示请求的所有环境变量, 包含所有请求的相关信息

            def index(request):
                # 封装所有用户请求信息
                # print(request.environ)
                for k, v in request.environ.items():
                    print(k, v)
                return HttpResponse('OK')

    - CBV
    - FBV

* Models的其他操作(反查等)


* Templates
    - 母版 抽取页面公用元素 其他模版继承该母版

            设置母版 需要子类填充的地方声明:
                {%block 变量名%}{% endblock %}

            在子类中:
                {%extends 'master.html'%} // 继承母版
                {%block 变量名%}需要填充的内容{% endblock %} // 实现母版中需要替换的内容
            这样在views渲染html的时候就能够替换成对应的html
            参考 master.html tp1, tp2, tp3

    - 在html中自定义函数

    - 模版导入
        一个html页面只能继承一个母版 不能继承多个母版
        但模板支持导入的功能 可以将页面抽离成组件 进行组件化构建页面

            {% include 'tag.html'%}
            参考tag.html, tp1.html
            可以在组件html中直接写变量和函数, django支持将数据渲染至页面组件中

    - 自定义模版函数与filter

            1.django提供filter: simplefilter 实际上是python函数

                {{ item.event_start|date:"Y-m-d H:i:s"}}
                {{ bio|truncatewords:"30" }}
                {{ my_list|first|upper }}
                {{ name|lower }}

            2.自定义filter
                1. 编写py文件 最多只能支持两个参数
                    @register.filter
                    def combine_str(str1, str2):
                        return str1 + str2

                2. 在html中引入
                    {% load custom_tpl_filter %}

                3. 调用filter
                     {{ "first str"|combine_str:" second str"}}

                   输出first str second str
                   参考tpl4.html

            3.自定义模板函数

                a、在app中创建 templatetags 模块

                b、创建任意 .py 文件，如：xx.py

                    #!/usr/bin/env python
                    #coding:utf-8
                    from django import template
                    from django.utils.safestring import mark_safe

                    register = template.Library()

                    @register.simple_tag
                    def my_simple_time(v1,v2,v3):
                        return  v1 + v2 + v3

                    @register.simple_tag
                    def my_input(id,arg):
                        result = "<input type='text' id='%s' class='%s' />" %(id,arg,)
                        return mark_safe(result)

                c、在使用自定义simple_tag的html文件中导入之前创建的 xx.py 文件名

                    {% load xx %}

                d、使用simple_tag

                    {% my_simple_time 1 2 3%}
                    {% my_input 'id_username' 'hide'%}

                    参考tpl4.html

            两种方式的用途
                1.自定义filter可以用于条件判断 也可以用于处理显示内容 但只支持最多两个参数
                    优点 可以作为if条件
                    缺点 参数有限制
                    {{ 参数1|函数名:参数2 }}
                    {% if "first str"|combine_str:" second str"%}
                    {%end if%}
                2.自定义函数可以用于页面内容的赋值计算和添加标签
                    优点 参数任意 空格区分
                    缺点 不能作为if条件判断

* 分页加载
    - Django分页加载 (只能用于django)
    - 自定义分页加载 (适用于所有python-web框架)

        防止XSS攻击:
            在分页处理中, 显示的分页按钮标签都应该在后台配置处理
            防止前端页面被注入js或html导致XSS攻击 因此提供两种处理方式:

            1.前端处理方式
                向django表明这段字符串是安全的 可以直接当作html语言使用
                {{str|safe}}

            2.后端处理方式

                from django.utils.safestring import mark_safe
                 str = """
                        <a href="/user_list?p=1">1</a>
                        <a href="/user_list?p=2">2</a>
                        <a href="/user_list?p=3">3</a>
                       """
                str = mark_safe(str)
                return render(request, 'user_list.html', {'user_list': li, 'str': str})

        分页处理

            # 测试数据 全局变量
            LIST = []
            for i in range(109):
                LIST.append(i)


            def user_list(request):
                """ 分页测试 """
                current_page = request.GET.get('p', 1)
                current_page = int(current_page)
                start = (current_page - 1) * 10
                end = current_page * 10
                # 获取应当给前端显示的item列表
                li = LIST[start: end]
                # 每页10条 求总页数和余数 如果余数大于0 则总页数需要加1
                page_count, remainder = divmod(len(LIST), 10)  # 求商和余数

                if remainder:
                    page_count += 1

                # 计算输出给前端的标签字符串
                page_str = ""
                for i in range(1, page_count+1):
                    page_str += '<a href="/user_list?p=%s">%s</a>\n' % (i, i)

                # 向django表明这段注入的标签字符串是安全的 可以正常显示
                from django.utils.safestring import mark_safe
                str = mark_safe(page_str)
                return render(request, 'user_list.html', {'user_list': li, 'page_str': page_str})



* cookie & session

    cookies:
        request.COOKIES

        是客户端浏览器上的一个文件 用键值对存储 用于存储一些用户的状态和token
        如登录之后 服务端会下发一个token给浏览器存储 之后客户端的每次请求 都会携带这个token
        客户端通过token去验证用户, 这样就不需要进行重复登录操作

        设置cookies 至 客户端
            res = redirect('/after_login/')
            # 如果不设置除k-v之外的其他参数 关闭浏览器后就失效 浏览器清空cookies
            res.set_cookie('cookies_username', u)

            rep.set_signed_cookie(key,value,salt='加密盐',...)
            参数：
                key,              键
                value='',         值
                max_age=None,     超时时间
                expires=None,     超时时间(IE requires expires, so set it if hasn't been already.)
                                      max_age 与expires 属性都是指定失效时间 max_age已经代替expires
                                      Expires指定一个绝对的过期时间 指从指定时间到1970.1.1的秒数
                                      max-age 指定的是从文档被访问后的存活时间，这个时间是个相对值 也是秒数
                                      为了兼容性 两个属性都需要设置

                path='/',         Cookie生效的路径，/ 表示根路径，特殊的：跟路径的cookie可以被任何url的页面访问
                domain=None,      Cookie生效的域名
                secure=False,     https传输
                httponly=False    只能http协议传输，无法被JavaScript获取（不是绝对，底层抓包可以获取到也可以被覆盖）
                                    但在document.cookie中是获取不到的 但并不代表安全 只是建议使用


            # 设置超时时间为100秒后
            response.set_cookie('key', 'value', max_age=100)  # 最大有效期为100秒 cookies被浏览器访问后触发计时
            response.set_cookie('key', 'value', expires=current_date)  # 失效日期为指定日期到1970.1.1的秒数

        删除cookies 常用于登出操作
            res.delete_cookie('cookies_username')

        服务器获取客户端的cookies
            value = request.COOKIES.get('cookies_username')
            value = request.COOKIES['cookies_username']

            request.get_signed_cookie(key, default=RAISE_ERROR, salt='', max_age=None)
            参数：
                default: 默认值
                   salt: 加密盐
                max_age: 后台控制过期时间

                参考 views.py

        由于cookie保存在客户端的电脑上，所以，JavaScript和jquery也可以操作cookie。
            <script src='/static/js/jquery.cookie.js'></script>
            $.cookie("list_pager_num", 30,{ path: '/' });

        cookie 前后端都能设置与修改 因此可以在前端修改 后台读取 进行页面控制
            参考user_list.html

                <script src="/static/jquery.cookie.js"></script>
                <script>
                    function changePageSize(ths) {
                        // 获取当前用户选择的值
                        var v = $(ths).val();
                        // 使用jquery设置cookie 用于后端读取
                        $.cookie('page_of_count', v);
                    }

                    $(function(){
                        // 获取cookies里选中的值
                        var select_val = $.cookie('page_of_count', {'path': '/user_list/'});
                        if (select_val) {
                            $('#sel').val(select_val);
                        }
                    });
                </script>




        带签名的cookie (加盐加密签名): 加盐要一一对应
            # 设置加盐加密签名
            response.set_signed_cookie('key', 'value', 'salt')
            # 获取加盐加密签名
            request.get_signed_cookie('key', 'salt')

    views装饰器处理: 如 用户认证

           登录的用户才能看 否则提示登录或返回主页
           用户认证 保存用户状态

           基于CBV / FBV 的用户认证装饰器

           装饰器:
                def auth(func):
                    def wrapper(request, *args, **kwargs):
                        username = request.COOKIES.get('cookies_username')
                        if not username:
                            # 如果cookie中没有用户名 说明未登录 跳转到登录
                            return redirect('/login/')
                        # 执行被装饰的函数 跳转页面由func自己处理 最后通过wrapper返回
                        return func(request, *args, **kwargs)

                     return wrapper

           FBV:
                @auth
                def after_login(request):
                    # 获取当前已登录用户名
                    # value = request.COOKIES.get('cookies_username')
                    #
                    # if not value:
                    #     # 如果用户名为空 则跳转到登录页面重新登录
                    #     return redirect('/login/')
                    # 如果加了装饰器 以上代码都不需要写
                    return HttpResponse("Login OK")


           CBV:
                # 可以直接在类上加装饰器 指明哪个请求方式需要加验证 可以直接加到dispatch上 表明所有请求方式都需要验证
                #@method_decorator(auth, name='dispatch')
                class Order(views.View):
                    """ CBV 用户认证 """
                    # @method_decorator(auth)
                    # def dispatch(self, request, *args, **kwargs):
                    #     """如果全部请求都需要认证 那么直接加到dispatch上就可以"""
                    #     return super().dispatch(request, *args, **kwargs)

                    @method_decorator(auth)
                    def get(self, request):
                        username = request.COOKIES.get('cookies_username')
                        # if not username:
                        #     # 如果cookie中没有用户名 说明未登录 跳转到登录
                        #     return redirect('/login/')
                        # 如果加了装饰器 以上代码都不需要写
                        return render(request, 'order.html', {'current_user': username})

                    @method_decorator(auth)
                    def post(self, request):
                        username = request.COOKIES.get('cookies_username')
                        # if not username:
                        #     # 如果cookie中没有用户名 说明未登录 跳转到登录
                        #     return redirect('/login/')
                        return render(request, 'order.html', {'current_user': username})




* Form验证 html验证与server验证
    ?


