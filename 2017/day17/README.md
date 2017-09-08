GET 获取数据
POST 提交数据

##### 路由系统URL

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