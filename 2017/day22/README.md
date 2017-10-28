##### 知识点概要

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

