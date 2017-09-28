#### 回顾

* Django 生命周期 路由系统url-视图函数views-模版渲染template + 数据组装- 返回字符串return string

* settings.py 配置

    1. 注册app 用于数据库创建
    2. 配置静态文件路径

            # 静态文件前缀 在template中使用的静态文件都会通过前缀去找寻STATICFILES_DIRS下的文件
            STATIC_URL = '/static/'

            # 配置静态文件目录路径
            STATICFILES_DIRS = (
                os.path.join(BASE_DIR, 'static'),
            )

            在html中使用:
                <link rel="stylesheet" href="/static/commons.css">


* 路由系统
    1. 固定url 与 func 或 class.as_view()对应
    2. 正则表达式, 设置接受参数名称(?P<nid>\d+)
    3. 设置别名 name="xxx" 模版中通过 {% url "xxx" %} 获取url
       获取当前页面url {{ request.path_info }}
    4. 通过别名获取url reverse()
    5. app中添加urls.py, project设置根路径 include("app.urls")

* 视图
    FBV: function base view
    CBV: class base view

    FBV:

        def index(request, *agrs, **kwargs):
            pass
    CBV:

        class Index(views.View):

             def dispatch(self, request, *args, **kwargs):
                result = super(Home, self).dispatch(request, *args, **kwargs)
                return result

            def post(self, request, *agrs, **kwargs):
                pass

            def get(self, request, *args, **kwargs):
                pass

    获取请求的数据

        request.POST.get("xxx")
        request.GET.get("xxx")
        request.POST.getlist("xxx")
        request.GET.getlist("xxx")
        request.FILES.get("xxx") # 获取 enctype="multipart/form-data"表单上传的文件

        获取上传的文件 保存在服务器
        import os
        file_path = os.path.join('upload', file_obj.name)
        f = open(file_path, mode='wb')
        # chunks 是上传文件的块 是一个生成器 需要迭代 也可直接遍历文件对象 内部会遍历chunks
        for block in file_obj.chunks():
            f.write(block)
            f.close()

    给用户返回数据

        return HttpResponse('xxx of string')
        return redirect('url') # code 302 跳转
        return render(request, 'path of html', {xxx: xxx, yyy: yyy}) # code 200 渲染


* 模版语言

    所有的对象内部属性调用都使用 "."

    获取单值

        {{}}

    for循环列表添加标签

        {% for i in list %}
            <li> {{ i.value }} </li>
        {% endfor %}

    for循环字典添加标签

        # user_dict.keys
        # user_dict.values

        {% for k, v in user_dict.items %}
            <li>{{k}} - {{v}}</li>
        {% endfor %}

* ORM

    1. 创建类与字段 写入数据库

            # id 不写也会自动生成 默认都不为空 max_length为字符长度
            class User(models.Model):
                id = models.AutoField(primary_key=True)
                age = models.IntegerField()
                name = models.CharField(max_length=32)

            生成要同步的数据
                python manager.py makemigrations
            执行同步
                python manager.py migrate

    2. 增

            #
            models.User.objects.create(
                name="xxx",
                age = 12
            )

            #
            dict = {'name': 'xxx', 'age': 12}
            models.User.objects.create(**dict)

            #
            obj = models.User(name='xxx', age=12)
            obj.save()

    3. 删

            models.User.objects.filter(id=1).delete()

    4. 改

            models.User.objects.filter(id=1).update(name='yyy')
            models.User.objects.filter(id=1).update(**dict)

    5. 查

            models.User.objects.filter(id=1) # return QuerySet
            models.User.objects.filter(id=1, name='xxx') # return QuerySet
            models.User.objects.filter(**dict) # return QuerySet



            models.User.objects.filter(id__gt=1) # > return QuerySet
            models.User.objects.filter(id__gte=1) # >= return QuerySet
            models.User.objects.filter(id__lt=1) # < return QuertSet
            models.User.objects.filter(id__lte=1) # <= return QuertSet


            dict = {'name': 'xxx', 'age__lte': 13}
            models.User.objects.filter(**dict) # name=xxx&&age<=13 return QuertSet



            models.User.objects.all() #所有 return QuerySet
            models.User.objects.all().first() # 第一个 return User
            models.User.objects.filter(id=1).first() # 第一个 return User

    6. 外键关联

            class UserType(models.Model):
                # 不写主键 自动生成一个自增的主键 字段名为id
                caption = models.CharField(max_length=32)
                # (1, 普通用户) (2, VIP用户) (3, 游客)

            class User(models.Model):
                age = models.IntegerField()
                name = models.CharField(max_length=10)
                # 约束条件 user_type 获取时user_type 为UserType对象
                # 数据库存储的列名为user_type_id 存储的是UserType的id
                user_type = models.ForeignKey("UserType",to_field='id', default=1)

    7. 从数据库获取列表数据三种方式

            # 获取所有业务线数据 只获取id与caption
            # businesses = models.Business.objects.all()
            # 没有values的情况
            # 返回QuerySet数据 继承于列表 内部为Business对象
            # [business(id, caption, english),..]

            businesses = models.Business.objects.all().values('id', 'caption')
            # 有values情况
            # 返回QuerySet 字典对象列表
            # [{id: xx, caption:xxx}, ...]

            # businesses = models.Business.objects.all().values_list('id', 'caption')
            # 有values情况
            # 返回QuerySet 元组对象列表
            # [(xx, xxx), ...]

    8. 获取单个数据

            # 获取id为1的单个对象, 如果不存在抛出异常
            business = models.Business.objects.get(id=1)
            # 获取id为1的列表中的第一个对象, 如果不存在则为空
            business = models.Business.objects.filter(id=1).first()

    9. 跨表多数据查询

            # 查询nid > 0 的host表的nid, hostname, bussiness_id, business_id对应business表的caption
            datas = models.Host.objects.filter(nid__gt=0)
                .values('nid', 'hostname', 'business_id', 'business__caption')

            # 双下划线代表跨表查询字段

            # django会通过双下划线进行split 然后去查询business表的caption字段
    10. html 循环中的属性

            <!--for循环的次数-->
            <td>{{ forloop.counter }}</td>
            <!--从0开始的for循环序号-->
            <td>{{ forloop.counter0 }}</td>
            <!--倒序 序号-->
            <td>{{ forloop.revcounter }}</td>
            <!--倒序 从0开始序号-->
            <td>{{ forloop.revcounter0 }}</td>
            <!--嵌套循环是 当前循环的父循环对象 包含上述所有信息-->
            <td> {{ forloop.parentloop }}</td>
            <!--最后一个-->
            <td> {{ forloop.last }}</td>
            <!--第一个-->
            <td> {{ forloop.first }}</td>

#### AJAX
    AJAX即“Asynchronous Javascript And XML”（异步JavaScript和XML），是指一种创建交互式网页应用的网页开发技术。
    AJAX = 异步 JavaScript和XML（标准通用标记语言的子集）。
    AJAX 是一种用于创建快速动态网页的技术。
    AJAX 是一种在无需重新加载整个网页的情况下，能够更新部分网页的技术。

    通过在后台与服务器进行少量数据交换，AJAX 可以使网页实现异步更新。这意味着可以在不重新加载整个网页的情况下，对网页的某部分进行更新。
    传统的网页（不使用 AJAX）如果需要更新内容，必须重载整个网页页面。

    如 登录操作 错误提示直接在输入框上方提示

##### 使用jquery 实现ajax

    注意ajax 请求 django需要返回HttpResponse

    $.ajax({
        url: '/host',
        type: "POST",
        data: {'k1': 123, 'k2': root},
        success : function(data) {
            // response 后台响应成功后触发的函数 data为响应的数据
        }
    })


    如: host.html

        $('#ajax_submit').click(function () {
               $.ajax({
                   url: '/test_ajax',
                   type: 'POST',
                   data: {
                       'hostname': $('#hostname').val(),
                       'ip': $('#ip').val(),
                       'port': $('#port').val(),
                       'business_id': $('#business_id').val()
                   },
                   success: function (data) {
                       if (data === 'OK') {
                           location.reload();
                       } else {
                           alert(data);
                       }

                   }
               })
            });


    以下三个方法实际上都是调用了$.ajax, 只是把type改成了get,post
    $.get(url='xxx', data={}, success=function(data){});
    $.getJson...
    $.post...


    建议: 永远让服务器返回一个字典
    dictObj = {'status': True, 'error': None, 'data': None}
    # ...
    return HttpResponse(json.dump(dictObj))

    注意 其实可以是发render的 但是返回的数据为整个html, 因为render返回的数据为html + 数据的渲染
        redirect其实也可以发 但是客户端不会有反应

#### js中json与对象的转换
       // 对象转换为字符串
       JSON.stringify(obj)
       // JSON解析为对象
       var ret = JSON.parse(data)

#### py中json与对象的转换
       import json
       // 对象序列化(释放)为字符串
       json.dump(obj)
       // JSON反序列化解析为对象
       ret = json.load(str)

#### 标签内容 序列化

       $('#edit_form').serialize(), // 将form下所有值打包成json发到后台


#### 表与表的多对多关系

    两张表存在多对多关系 需要第三张表去维护这两张表的关系
    如一个Host中可以有多个Application
    一个Application中可以有多个Host
    如果需要查询host中的app 或app所在的host 则需要第三张表去关联这两张表的关系

    1. 方式一 自定义关系表: 建立一个关系表 持有另外需要建立两个关系的外键
        class HostToApp(models.Model):
            """Host 与 Application 关系表"""
            # host表主键 host_id
            host = models.ForeignKey(to='Host', to_field='nid')
            # application表主键 app_id
            app = models.ForeignKey(to='Application', to_field='id')

        建立host与app关系:

            models.HostToApp.objects.create(host_id=1, app_id=2)

    2. 方式二 Django自动创建第三张表
        class Application(models.Model):
            """应用表"""
            name = models.CharField(max_length=32)
            # django自动创建多对多关系表HostToApp
            relation = models.ManyToManyField('Host')


        表中存在三个字段 id, application_id, host_id 表名为 app01_relation

        对第三张表进行操作

            1. 添加
                建立host与app关系: 无法直接对第三张表进行操作 可以间接操作
                app = models.Application.objects.filter(id=1).first()

                # 在第三张表中使id=1的app与 host表id=2的行建立关系
                app.relation.add(2)

                # 同时建立多个关系 在第三张表中使id=1的app与host表id=2,3,4,5的行建立关系
                app.relation.add(*[2, 3, 4, 5])
                app.relation.add(2, 3, 4, 5)

            2. 删除
                app = models.Application.objects.filter(id=1).first()
                app.relation.remove(2)
                app.relation.remove(2, 3, 4, 5)
                app.relation.remove(*[2, 3, 4, 5])

               清空与当前app与所有host的关联关系
                app.relation.clear()

            3. 修改关联关系
                app.relation.set([3, 5, 7])
                set操作相当于clear后重新add







    建议: 两种方式结合使用 如果关系表中字段只存在 id 和另外两个表的主键 建议使用第二种方式 即自动创建只能生成3列字段
          如果有更多的字段 则自定义创建 扩展性比较高
