GET 获取数据
POST 提交数据

##### 路由系统URL
        1.支持CBV FBV
            CBV
                url(r'^home/', views.Home.as_view()),
            FBV
                url(r'^home/', views.home),

        2. 路由系统正则与拼接, 通过url拼接或正则
            从而实现跳转(如 用户列表跳转到用户详情url)

            但是在SEO排名中, 拼接url的页面的排序低于正则url
            也就是说动态页面排序低于静态页面
            因为url拼接后相当于GET请求携带参数, 会认为是动态页面
            如 detail?nid=1 认为是动态的
            而 detail-1 认为是静态的

            2.1 拼接url
            urls.py:

                url(r'^detail/', views.detail),
            views.py:

                def detail(request):
                    """获取拼接url中的数据"""
                    # return HttpResponse("detail")
                    nid = None
                    if request.method == "GET":
                        nid = request.GET.get('nid')
                        detail_info = USER_DICT[nid]
                    return render(request, 'detail.html', {'detail_info': detail_info})
            html:

            <ul>
                <!-- _blank 指打开一个新页 -->
                {% for k, v in user_dict.items%}
                    <li><a target="_blank" href="/detail/?nid={{ k }}">{{ v.name }}</a></li>
                {% endfor %}
            </ul>

            2.2 正则实现url
            urls.py:

                url(r'^detail-(\d+)', views.detail)

            views.py

                def detail(request, nid):
                    """获取正则url中的数据
                        url: detail-1
                        reg: detail-(\d+)
                        第二个参数是根据urls.py 定义的url正则中的括号包裹的数据返回的
                        这里返回1
                    """
                    detail_info = USER_DICT[nid]
                    return render(request, 'detail.html', {'detail_info': detail_info})

            html:

                 <ul>
                    <!--url正则方式跳转-->
                    {% for k, v in user_dict.items %}
                    <li><a href="/detail-{{ k }}" target="_blank">{{ v.name }}</a></li>
                    {% endfor %}
                 </ul>

                 2.2.1
                    正则表达式分组:
                         第一个匹配的赋值给uid 第二个匹配的赋值给uid 设定了分组 调用函数时就无关顺序
                         url(r'^detail-(?P<uid>\d+)-(?P<nid>\d+)', views.detail)

                          def detail(request, nid, uid):
                                pass

              2.3 可变长度参数接收

                    def detail(request, *args, **kwargs)
                        """
                        不指定分组的方式通过*args方式接收 为元组
                        指定分组的方式通过**kwargs方式接收 为字典

                        """
                        pass

        3. url 设置别名:
            在开发中 有可能需要频繁的修改url名称, 这样就导致了url.py的url需要频繁修改
            html中如果存在表单 action也需要修改 就造成了修改复杂

            在django中 提供了一种便利的方式 只需要给url添加别名 html的action设置别名即可
            这样在修改url后 不需要再去修改html文件

            参考index.html
             url(r'^index/', views.index, name='index_alias'),  # 设置别名
             <form action="{% url 'index_alias' %}" method="post"></form>

             3.1 子path配置

                 1. 固定path  向index/childpath 提交
                     url(r'^index/(\w+)', views.index, name='index_alias')
                     <form action="{% url 'index_alias', 'childpath' %}" method="post"></form>



                 2. 分组  向index/3/1 提交
                      url(r'^index/(?P<uid>\d+)/(?P<nid>\d+)', views.index, name='index_alias')
                      <form action="{% url 'index_alias', nid=1, uid=3 %}" method="post"></form>


                    这种方式 可以用于从指定页面跳转至登录注册操作后跳转回指定页面:
                        在跳转登录时 传递当前页面path给登录页面, 登录页面action为跳转前页面的path 可以实现回到指定页面

             3.2 反转: 通过别名 获取url
                 url(r'^index/', views.index, name='index_alias')

                 views.py
                    from django.urls imports reverse
                    v = reverse('index_alias') # index/

                3.2.1 可变childpath
                    url(r'^index/(\d+)', views.index, name='index_alias')

                    views.py
                        from django.urls imports reverse
                        v = reverse('index_alias', (18,)) # index/18

                3.2.1 分组childpath
                    url(r'^index/(?P<nid>\d+)', views.index, name='index_alias')

                    views.py
                        from django.urls imports reverse
                        v = reverse('index_alias', kwagrs={'nid': 18}) # index/18


        4. 获取当前url path :
            request.path_info
            向当前页面url提交post请求
            url配置
                url(r'^index/(w+)', views.index, name='index_alias')
            html配置
                <form action="{{request.path_info }}" method="post"></form>

            接收:
                def index(request, child_path):
                    # child_path = 'childpath'
                    print(request.path_info) # index/childpath





##### 视图 View
    1. 请求对象
        request.POST    表单提交都从POST中接收
        request.GET     url提交都从GET接收
        request.FILES   文件提交都从FILE接收 html的form要加enctype="multipart/form-data"

    2. 获取请求数据
        1.获取单个数据:
            single_val = request.POST.get('gender')
        2.获取相同name的多个数据:
            multi_val = request.POST.getlist('favour')

        3.获取上传的文件
            file_obj = request.FILES.get('upload_file')
            if file_obj is not None:
                print('获取上传文件', file_obj, type(file_obj))
                print('文件名称', file_obj.name)
                # 获取上传的文件 保存在服务器
                import os
                file_path = os.path.join('upload', file_obj.name)
                f = open(file_path, mode='wb')
                # chunks 是上传文件的块 是一个生成器 需要迭代
                for block in file_obj.chunks():
                    f.write(block)
                f.close()
            else:
                print('文件为空')

        4. FBV, CBV
            在urls.py 封装的url与函数的对应关系 叫做FBV
            function base view

            类与url对应, 如jsp, 叫做CBV
            class base view

            在Django中 两种绑定方式都支持

            CBV 写法与FBV不同:

                url需要配置
                    url(r'^home/', views.Home.as_view()),

                views中的调用类写法如下:
                    class Home(View):
                        """class base view"""

                        def get(self, request):
                            # get请求执行 写法同fbv
                            pass

                        def post(self, request):
                            # post 请求执行
                            pass

                父类View中包含dispatch方法, 会通过反射(getAttr)获取外部设置的get和post函数
                进行分发调用, 可以重写dispatch 进行请求处理前的逻辑封装

        5. 装饰器
            pass

        6. 路由分发
            原因: 在project中 可以有多个app, 但是urls.py只有一个, 多人开发时有可能导致同时改动的冲突
                在django中 支持路由分发模式, 即:
                    在project的urls.py指定一个父path, 与父path相关的子path写到对应的app下的urls.py中

                    参考例子cmdb相关文件 url:cmdb/login

            project-urls.py:
                # cmdb模块路由分发模式
                url(r'^cmdb/', include("cmdb.urls"))

            cmdb-urls.py
                urlpatterns = [
                    # cmdb模块路由分发模式
                    # url 为 cmdb/login
                    url(r'^login/', views.cmdb_login)
                ]

        7. 默认值:

        8. 命名空间





##### 模板 Template

        1. 遍历列表
             {% for row in user_list %}
                <li>{{row.name}}</li>
            {% endfor %}

        2. 遍历字典

            <!-- 遍历字典的时候 是无序的
                user_dict.keys # 键
                user_dict.values # 值
                user_dict.items # 键值对
             -->
            <ul>
                {% for k, v in user_dict.items %}
                    <li>{{k}} - {{v}}</li>
                {% endfor %}
            </ul>

##### Django-ORM操作
      原生sql语句与django orm语句都是有对应关系的
      我们需要学习的就是这套对应关系
      增删改查 1对1 1对多 多对多

        select * from tb where id > 1
        models.tb.objects.filter(id__gt=1)

        select * from tb where id < 1
        models.tb.objects.filter(id__lt=1)

        select * from tb where id = 1
        models.tb.objects.filter(id=1)

    默认使用sqlite数据库

    修改为mysql:
        DATABASES = {
        'default': {
        'ENGINE': 'django.db.backends.mysql',
        # 注意 数据库名称 django不能创建 因此需要先在mysql命令行创建数据库名称
        # 再在配置文件中填写数据库名称
        'NAME':'dbname',
        'USER': 'root',
        'PASSWORD': 'xxx',
        'HOST': '',
        'PORT': '',
        }
    }

    *******************注意******************
    django连接mysql数据库默认使用MySQLdb模块
    但是这个模块python3没有, 需要使用pymysql模块
    因此需要做一些配置 在project的__init__.py中需要添加:

    import pymysql
    pymysql.install_as_MySQLdb()

    这是告诉django安装了MySQLdb模块 实际使用的是pymysql的代码
    *****************************************

    1. 根据类自动创建数据库表
       1.1 app 下的models.py
        创建数据建构

        class UserInfo(models.Model):
            # 需要继承models.Model
            # 默认创建一个id列 自增 主键
            # 用户名列 字符串类型 指定长度
            username = models.CharField(max_length=32)
            password = models.CharField(max_length=64)

       1.2 在project-settings.py INSTALLED_APPS 注册app

       1.3
            更新表结构 此时数据库结构在内存中 makemigrations: 生成需要同步的数据
            ******   python manage.py makemigrations
            同步表结构至数据库 写入数据库存储 表名叫app01_userinfo migrate: 同步数据
            ******    python manage.py migrate

       1.4 增
            1. 第一种方式
                models.UserInfo.objects.create(
                    username='root',
                    password='123'
                )

                或者
                # dict = {'username': 'matt', 'password': '789'}
                # # dict为字典 **dict为将字典数据遍历放置到参数中
                # models.UserInfo.objects.create(**dict)

            2. 第二种方式
                # 实例化一个对象
                obj = models.UserInfo(username='admin', password='345')
                # 保存至数据库
                obj.save()

       1.5 查

            # 查询所有数据
            allSelect = models.UserInfo.objects.all()
            for i in allSelect:
                print(i.username)

            # 条件查询
            whereSelect = models.UserInfo.objects.filter(id=1)
                for i in whereSelect:
                print(i.username)
            返回的类型为Django提供的QuerySet类型 理解为一个列表 列表里是UserInfo对象

            # 只获取一条数据 如果不存在则报错 需要try-catch
            obj = models.UserInfo.objects.get(id=1)


       1.6 删
            # 删除所有
            models.UserInfo.objects.all().delete()
            # 条件删除
            models.UserInfo.objects.filter(id=4).delete()

       1.7 更新

            # 更新所有密码
            models.UserInfo.objects.all.update(password=123456)
            # 条件更新
            models.UserInfo.objects.filter(id=3).update(password=123456)


       1.8 获取查询结果的第一个对象
            whereSelect = models.UserInfo.objects.filter(id=1).first()
       1.9 获取查询结果的数量
            whereSelect = models.UserInfo.objects.filter(id=1).count()

       2.0 获取查询结果的sql语句
            whereSelect = models.UserInfo.objects.filter(id=1)
            whereSelect.query

#### Django 数据库表结构操作
    1. 增加列时 之前数据库存储的数据需要进行处理, django在生成数据库的列时
        默认都是不为空的 因此在同步表结构时 会提示是否设置为空 或在为空时设置默认数据

    2. 在mysql中 每个表只能有一个自增列 作为主键 如果不手动设置自增+主键 django会设置一个默认的列 "id" 作为主键

```
Please select a fix:
 1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
 1. 设置一个默认值 给之前该列为空的数据
 2) Quit, and let me add a default in models.py
 2. 退出 手动设置默认值或设置默认为空
```

    2. 设置列允许为空
        gender = models.CharField(max_length=10, null=True)  # 允许为空

    3. 删除列
        将class中对应的列删除并同步数据库即可

    4. 字段类型
        字符串
            CharField 字符串
            EmailField 邮箱字符串 (用于admin后台管理)
            UrlField Url字符串 (用于admin后台管理)
            GenericIPAddressField ipv4 ipv6 字符串
        数字

        时间

        二进制



        如果是用EmailField或UrlField 在管理后台添加或修改行数据 如果格式错误会进行提示

        更多
        {@link: http://www.cnblogs.com/wupeiqi/articles/5246483.html#基本结构 }


    5. 替换默认主键
          # 创建一个自增的列 并设置为主键 django将不再设置默认的id列
          uid = models.AutoField(primary_key=True)

          * 注意 自增必须设置为主键