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



#### Django ORM
    一对多创建