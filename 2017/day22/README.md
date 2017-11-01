##### 知识点概要
- select_related()数据库查询优化

        class Person(models.Model);
            name = models.CharField('作者姓名', max_length=10)
            age = models.IntegerField('作者年龄')

        class Book(models.Model):
            person = models.ForeignKey(Person, related_name='person_book')
            title = models.CharField('书籍名称', max_length=10)
            pubtime = models.DateField('出版时间')

        select_related()函数用于querySet查询结果集的优化
            如:在外键关联表中 如果在book表查询person的name时
            我们一般会执行
            p = book.person
            p.name
            实际上就相当于通过外键person_id(Book表的实际存储字段)获取person表对象
            再通过person对象获取name
            这就相当于进行了两次数据库查询 效率比较低

        使用select_related() 相当于对querySet结果集优化 在查询时执行了left_join|inner_join
        即 在第一次查询的时候就进行了并联查询 通过一次查询获取到你需要的数据 而不重复操作数据库

        那么 使用select_related()可以这样查询:
        p = models.Person.objects.all().select_related(person__name)
        p.name

        也可以(慎用, 外键层级复杂会查询异常 有最大递归查询上限 超出会跳出递归)
        models.Person.objects.all().select_related() # 一次性获取person中的所有字段, 尽可能多的获取所有外键关联和外键的表的其他外键关联的表的字段

        也可以
        models.Person.objects.all().select_related(depth=2) # 查询深度为2层 即当外键表中还有其他外键时不会再查询

        参考: http://blog.jobbole.com/74881/

        注意 select_related() 不支持多对多表的查询 仅支持一对多的查询





- ModelForm补充

        Model
            - 数据库操作
            - 验证
        Form
            - class LoginForm(Form):
                email = fields.EmailField()
            - is_valid -> 每一个字段进行正则(字段内置正则) + clean_字段
                -> clean(__all__) -> _post_clean

            - clean_data (验证通过 原数据)
            - errors (错误html, as_json() 转换为json)

        ModelForm

            Model + Form => 验证 + 数据库操作

                如果又有Form 又有ModelForm 二者验证正则相同 那么就会写重复代码
                应在ModelForm中使用From中的字段

            Form 继承 BaseForm 存在is_valid()
            ModelForm 继承BaseModelForm 继承BaseForm
            也就是说 BaseForm 中的函数 ModelForm函数也支持

            models.py:
                class UserInfo(models.Model):
                    # verbose_name 用于后台管理和modelform的label显示
                    # 也可以使用Meta的labels
                    username = models.CharField(verbose_name='用户名', max_length=32)
                    email = models.EmailField()
                    user_type = models.ForeignKey(to='UserType', to_field='id')

            views.py

                 class UserInfoModelForm(forms.ModelForm):
                    class Meta:
                        # 指定数据库的类
                        model = models.UserInfo
                        # 指定显示所有字段
                        fields = '__all__'
                        # 指定只显示username字段
                        # fields = ['username',]
                        # 排除, 不显示email字段
                        exclude = ['email',]
                        labels={'username': '用户名',},                     # 提示信息
                        help_texts={'username': '输入的是用户名',},# 帮助提示信息 跟在input标签后面
                        widgets= {
                            'username': Fwidgets.Textarea(attrs={'class': 'c1'})
                        },                    # 自定义插件 from django.forms import widgets as Fwidgets
                        error_messages={

                             '__all__': {     # 定义整体错误信息
                                'required': '不能为空',
                                'invalid': '格式不对'
                             },
                             'email': {
                                'required': '邮箱不能为空',
                                'invalid': '邮箱格式不对'
                             }
                        },             # 自定义错误信息（整体错误信息from django.core.exceptions import NON_FIELD_ERRORS）
                        field_classes={
                            'email': Ffield.URLField # 在前端页面正则验证时 不再是model中的邮箱格式验证 而是url格式
                        }              # 自定义字段类型 （也可以自定义字段）
                        localized_fields=('birth_date',) # 本地化，如：根据不同时区显示数据
                        如：
                            数据库中
                                2016-12-27 04:10:57
                            setting中的配置
                                TIME_ZONE = 'Asia/Shanghai'
                                USE_TZ = True
                            则显示：
                                2016-12-27 12:10:57

                 接受表单并进行数据库操作:

                    def index(request):
                        if request.method == 'GET':
                            form = UserInfoModelForm()
                            return render(request, 'index.html', {'form': form})

                        elif request.method == 'POST':
                            form = UserInfoModelForm(request.POST)
                            res = form.is_valid() # 验证是否有效
                            if res:
                                # 使用modelform可直接保存至数据库 比form获取cleaned_data再保存更简单
                                # 支持多对多的表存储 内部执行当前表-UserInfo的存储和内部的m2m多对多关系的存储
                                form.save()

                                #只进行当前表实例存储 不进行多对多存储:
                                instance = form.save(False)
                                instance.save()
                                # 多对多表的存储
                                form.save_m2m()
                            return redirect('/index/')


- Ajax

    - 原生XmlHttpRequest
    - jQuery
    - 伪Ajax操作

- 文件上传(预览)

    - Form提交: 缺点 刷新页面
    - Ajax上传文件

- 图片验证码(PIL模块) + Session(不能使用cookie)

- 富文本编辑框(加粗等)

    - CKEditor
    - UEEditor
    - TinyEditor
    - KindEditor

        - 基本使用
        - 文件上传/多文件上传/文件空间管理
        - 防止 XSS 攻击(接受客户端请求字符串中的指定字符, 过滤函数和标签)

