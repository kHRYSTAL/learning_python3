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

    - 自定义模版函数

            1.django提供函数: simplefilter 实际上是python函数

                {{ item.event_start|date:"Y-m-d H:i:s"}}
                {{ bio|truncatewords:"30" }}
                {{ my_list|first|upper }}
                {{ name|lower }}

            2.自定义模板函数

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

* cookie & session
    views装饰器处理: 如 用户认证
           登录的用户才能看 否则提示登录或返回主页
    用户认证 保存用户状态
    request.COOKIES

* 分页加载
    - Django分页加载 (只能用于django)
    - 自定义分页加载 (适用于所有python-web框架)

* Form验证 html验证与server验证


