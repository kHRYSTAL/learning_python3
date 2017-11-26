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
        p = models.Person.objects.all().select_related(person)
        p.name

        也可以(慎用, 外键层级复杂会查询异常 有最大递归查询上限 超出会跳出递归)
        models.Person.objects.all().select_related() # 一次性获取person中的所有字段, 尽可能多的获取所有外键关联和外键的表的其他外键关联的表的字段

        也可以
        models.Person.objects.all().select_related(depth=2) # 查询深度为2层 即当外键表中还有其他外键时不会再查询

        注意 外键的外键需要使用双下划线

        参考: http://blog.jobbole.com/74881/
             http://www.cnblogs.com/wt11/p/6392972.html


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

                 设置modelForm 表单的默认选中:
                    user_obj = models.UserInfo.objects.filter(id=nid).first()
                    # 页面显示的表单  # 将user_obj 设置为表单中的默认数据
                    mf = UserInfoModelForm(instance=user_obj)

                    return render(request, 'user_edit.html', {'mf': mf})

                 注意:

                    在html表单中设置数据库表某行数据为默认数据可以使用
                        mf = UserInfoModelForm(instance=user_obj)

                    更新表数据在save时也需要指定instance
                    user_obj = models.UserInfo.objects.filter(id=nid).first()
                    # 如果验证成功 需要update, 只使用save()是创建 因此也需要设置指定的默认数据
                    mf = UserInfoModelForm(request.POST, instance=user_obj)
                    if mf.is_valid():
                        mf.save()

                 ModelFrom 记录额外字段

                     class UserInfoModelForm(forms.ModelForm):
                        # 定义额外字段 记住登录状态 与数据库表无关
                        is_remember = fields.CharField(
                            widget=Fwidgets.CheckboxInput()
                            )

                     mf = UserInfoModelForm(request.POST)
                     if mf.is_valid():
                        print(mf.cleaned_data.get('is_remember')) # 保存到session
                        mf.save()


                 总结 ModelForm 能够帮助生成Html标签
                    内部类class Meta 能够帮助生成各种各样的标签
                    可以在生成html标签时设置默认值
                    mf = xxxModelForm(instance= ModelObj)

                    可以定制额外的标签 与class Meta同级
                    通过 mf.clean_data.get(xxx) 接收
                    验证规则使用is_valid() 通过勾子函数判断是否验证通过 勾子函数可以在Meta类中定义
                    数据库新增和更新使用save() 在mf初始化时通过instance区分
                    save_m2m()可以对多对多关系 进行多张表数据的存储 当表中存在多对多关系时 save() 默认为多对多存储
                    使用save(False) 可以不对多张表进行存储 只对当前表进行存储





- Ajax操作

    - 原生XmlHttpRequest

            ajax是浏览器XmlHttpRequest 和 ActiveXObject这些原生请求对象的上层封装

            参考
                http://www.cnblogs.com/wupeiqi/articles/5703697.html

            创建对象
                var a = new XMLHttpRequest();

                a. void open(String method,String url,Boolen async)
                   用于创建请求

                   参数：
                       method： 请求方式（字符串类型），如：POST、GET、DELETE...
                       url：    要请求的地址（字符串类型）
                       async：  是否异步（布尔类型）

                b. void send(String body)
                    用于发送请求

                    参数：
                        body： 要发送的数据（字符串类型）

                c. void setRequestHeader(String header,String value)
                    用于设置请求头

                    参数：
                        header： 请求头的key（字符串类型）
                        vlaue：  请求头的value（字符串类型）

                d. String getAllResponseHeaders()
                    获取所有响应头

                    返回值：
                        响应头数据（字符串类型）

                e. String getResponseHeader(String header)
                    获取响应头中指定header的值

                    参数：
                        header： 响应头的key（字符串类型）

                    返回值：
                        响应头中指定的header对应的值

                f. void abort()

                    终止请求

           XMLHttpRequest 属性

                a. Number readyState
                   状态值（整数）

                   详细：
                      0-未初始化，尚未调用open()方法；
                      1-启动，调用了open()方法，未调用send()方法；
                      2-发送，已经调用了send()方法，未接收到响应；
                      3-接收，已经接收到部分响应数据；
                      4-完成，已经接收到全部响应数据；

                b. Function onreadystatechange
                   当readyState的值改变时自动触发执行其对应的函数（回调函数）

                c. String responseText
                   服务器返回的数据（字符串类型）

                d. XmlDocument responseXML
                   服务器返回的数据（Xml对象）

                e. Number states
                   状态码（整数），如：200、404...

                f. String statesText
                   状态文本（字符串），如：OK、NotFound...

        注意:

                       function Ajax1() {
                        if (window.XMLHttpRequest) {// code for IE7+, Firefox, Chrome, Opera, Safari
                            xmlHttpRequest = new XMLHttpRequest();
                        }
                        else {// code for IE6, IE5
                            xmlHttpRequest = new ActiveXObject("Microsoft.XMLHTTP");
                        }
                        xmlHttpRequest.open("POST", '/ajax_json/', true);
                        // 设置请求头
                        csrftoken = getCookie('csrftoken');
                        xmlHttpRequest.setRequestHeader("key", "value");
                        // post请求时有csrf时需要设置请求头 如果django加了csrf校验 在回传给前端时会在cookies中
                //      xmlHttpRequest.setRequestHeader('X-CSRFToken', csrftoken);
                        // 如果为post请求需要设置请求头
                        xmlHttpRequest.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");

                        xmlHttpRequest.onreadystatechange = function () { // 接收事件回调
                            if (xmlHttpRequest.readyState == 4) { // 4表示接收response完成 一般还需要判断状态码为200
                                console.log(xmlHttpRequest.responseText); // 输出字符串
                                console.log(xmlHttpRequest.responseXML); // 输出字符串转换的标签 XMLDocument对象
                                console.log(xmlHttpRequest.status); // 服务端返回的状态码
                                resp = JSON.parse(xmlHttpRequest.responseText);

                            }
                        };
                        xmlHttpRequest.send("name=root;pwd=123");

                参考 ajax_test.html

    - jQuery

                jQuery的ajax

                $.ajax({
                    url: '/host',
                    type: "POST",
                    data: {'k1': 123, 'k2': root},
                    success : function(result,status,xhr) {
                        // 如果不想使用ajax封装好的result, 可以直接使用第三个参数xhr
                        // xhr就是XMLHttpResponse对象 可以进行原生ajax操作
                    }
                });

    - 伪Ajax操作 :

            iframe 在页面中包含独立的一块页面 通过url 可以显示不同的网页,
            iframe页面是独立于整个页面的 因此也是局部刷新

    - 上传文件三种方式:

            function xhrSubmit() {
                // 获取 需要上传的文件对象
                var fileObj = document.getElementById('upload').files[0];
                var xmlHttpRequest = new XMLHttpRequest();

                var formData = new FormData();
                formData.append('username', 'root'); // key-value;
                formData.append('file', fileObj);
                xmlHttpRequest.open("POST", '/upload_file/', true);
                xmlHttpRequest.onreadystatechange = function () { // 接收事件回调
                    if (xmlHttpRequest.readyState == 4) { // 4表示接收response完成 一般还需要判断状态码为200
                        console.log(xmlHttpRequest.responseText); // 输出字符串
                        console.log(xmlHttpRequest.responseXML); // 输出字符串转换的标签 XMLDocument对象
                        console.log(xmlHttpRequest.status); // 服务端返回的状态码
                        resp = JSON.parse(xmlHttpRequest.responseText);

                    }
                };
                xmlHttpRequest.send(formData);
            }

            function jQSubmit() {
                var fileObj = document.getElementById('upload').files[0];
                var formData = new FormData();
                formData.append('username', 'root'); // key-value;
                formData.append('file', fileObj);

                $.ajax({
                    url: '/upload_file/',
                    type: 'POST',
                    data: formData,
                    processData: false,
                    contentType: false,
                    success: function (arg, a1, a2) {
                        console.log(arg);
                        console.log(a1);
                        console.log(a2);
                    }
                });
            }

            function iframeSubmit() {
                // 提交成功后在onLoad时触发
                $('#ifm1').load(function () {
                    var text = $('#ifm1').contents().find('body').text();
                    var obj = JSON.parse(text);
                    console.log(obj);
                });
            }

            参考 upload.html

    - 使用上述Ajax操作的时机与选择

            纯字符串或Json操作 如果允许使用JQuery, 否则使用XMLHttpResponse 最次是iframe

            url, 上传文件, 优先选择iframe 因为jQuery 与 XMLHttpResponse 依赖form标签 同时需要自己封装预览效果






- HttpResponse自定义状态码与Message

        def ajax_json(request):
            ret = {'status': True, 'data': None}
            import json
            return HttpResponse(json.dumps(ret), status=404, reason="找不到页面")  # 自定义状态码

- 文件上传(预览)

    - Form提交: 缺点 需要刷新页面

    - Ajax上传文件

- 图片验证码(PIL模块) + Session(不能使用cookie)

        图形验证码一般是通过session存储的 在用户get请求至页面时 通过pil生成图形验证吗 并把验证码字符串存储到session中
        用户提交post请求时 获取用户发送的验证码 与 seesion中的验证码进行对比

        在服务器的session中 每个用户一块存储空间

        流程
            1 用户GET访问/login/
                - 创建一个验证码图片(PIL)
                - Session存放图片上的验证码
                - 返回给用户

            2 用户POST提交数据至/login/
                - 将验证码与Session存放的数据进行校验




- 富文本编辑框(加粗等)

    - CKEditor
    - UEEditor
    - TinyEditor
    - KindEditor

        - 基本使用
        - 文件上传/多文件上传/文件空间管理
        - 防止 XSS 攻击(接受客户端请求字符串中的指定字符, 过滤函数和标签)

