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
                {%extends 'master.html'%}
                {%block 变量名%}需要填充的内容{% endblock %}
            这样在views渲染html的时候就能够替换成对应的html
            可以多继承

    - 在html中自定义函数

* cookie & session
    views装饰器处理: 如 用户认证
           登录的用户才能看 否则提示登录或返回主页
    用户认证 保存用户状态
    request.COOKIES

* 分页加载
    - Django分页加载 (只能用于django)
    - 自定义分页加载 (适用于所有python-web框架)

* Form验证 html验证与server验证


