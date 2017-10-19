from django.shortcuts import render, redirect, HttpResponse

# Create your views here.


# region Session测试
def login(request):
    # from django.conf import settings
    # django自带的csrftoken别名
    # print(settings.CSRF_HEADER_NAME)
    # # HTTP_X_CSRFTOKEN
    # # X-CSRFtoken

    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        # 是否勾选自动登录
        remember = request.POST.get('remember', None)
        if user == 'root' and pwd == '123':
            # 生成随机字符串
            # 写到用户浏览器cookie
            # 保存至session中 key为随机字符串 value为用户相关信息
            # django 会自动执行以上所有操作 只需要一行代码
            request.session['username'] = user
            request.session['is_login'] = True
            # 判断是否勾选自动登录 单位为秒
            if remember:
                request.session.set_expiry(60 * 10)
            return redirect('/index/')
        else:
            print('用户名密码不正确')
            return render(request, 'login.html')


def index(request):
    if request.session.get('is_login', False):
        return render(request, 'index.html', {'username': request.session['username']})
    else:
        return HttpResponse('滚')


def logout(request):
    request.session.clear()
    return redirect('/login/')
# endregion


# region middleware 测试
class Foo:
    """ 测试middleware process_template_response是否执行 """
    def __init__(self):
        super().__init__()

    def render(self):
        return HttpResponse('test_middleware')


def test_middleware(request):
    """ 测试自定义中间件 """
    print("test_middleware")
    return Foo()
# endregion


# region 缓存测试
from django.views.decorators.cache import cache_page

# 单位为秒 默认为300秒 此配置比默认配置优先级高, 即在指定事件内使用缓存 超过时间 缓存失效
# @cache_page(60 * 15)
def cache(request):
    import time
    current_time = time.time()
    return render(request, 'cache.html', {'ctime': current_time})
# endregion


# region 信号测试
def signal(request):
    """ 需求: 在每次save时记录数据库操作日志 """
    from app01 import models
    obj = models.UserInfo(user='root')
    obj.save()

    obj = models.UserInfo(user='root')
    obj.save()

    obj = models.UserInfo(user='root')
    obj.save()
    return HttpResponse("测试Django信号接受")


def custom_signal(request):
    """ 自定义信号 需要手动发送信号触发 """
    from signal_receiver import pizza_done
    pizza_done.send(sender='khrystal', toppings=123, size=456)
    # 接收到的数据
    # khrystal {'signal': <django.dispatch.dispatcher.Signal object at 0x1017ce7f0>, 'toppings': 123, 'size': 456}
    return HttpResponse("测试自定义信号")
# endregion


# region 表单验证
from django import forms
from django.forms import widgets
from django.forms import fields


class MyForm(forms.Form):
    """ 指定客户端发送的表单提取的字段 表单的name必须与变量名相同"""
    user = fields.CharField(
        label='用户名',
        initial='初始值',
        # 自定义正则表达式验证
        # validators=[RegexValidator(r'^[0-9]+$', '请输入数字'), RegexValidator(r'^159[0-9]+$', '数字必须以159开头')],
        # 自定义样式 专门用于生成html 不写默认为input
        widget=widgets.Textarea(attrs={'class': 'c1', 'style': 'height: 40px', 'placeholder': '用户名'}),
        # 错误信息提示
        error_messages={'required': '用户名不能为空'}
    )
    pwd = fields.CharField(
        label='密码',
        # widget=widgets.TextInput(attrs={'placeholder': '密码', 'type': 'password'}),
        widget=widgets.PasswordInput(attrs={'placeholder': '密码'}),
        max_length=12,
        min_length=6,
        error_messages={'required': '密码不能为空', 'min_length': '密码长度不能小于6', 'max_length': '密码长度不能大于12'}
    )
    email = fields.EmailField(
        label='邮箱',
        widget=widgets.TextInput(attrs={'placeholder': '邮箱'}),
        error_messages={'required': '邮箱不能为空', 'invalid': '邮箱格式错误'}
    )

    path = fields.FilePathField(path='app01')

    city = fields.ChoiceField(
        choices=[(0, '上海'), (1, '北京'), (2, '天津')]
    )


from app01 import models


def test_form(request):
    if request.method == 'GET':
        # GET 请求 只提供表单 内部会进行require 和 长度 格式的处理
        form = MyForm()
        # GET 请求设置默认值
        # dic = {
        #     'user': 'khrystal',
        #     'pwd': '123',
        #     'email': 'khrystal0918@gmail.com',
        #     'path': 0,
        #     'city': 1,
        # }
        # form = MyForm(initial=dic)
        return render(request, "form_test.html", {'form': form})
    elif request.method == 'POST':
        # 获取用户所有的数据
        form = MyForm(request.POST)
        # 每条数据请求的验证是否通过 res为boolean
        res = form.is_valid()
        print(res)
        if res:
            # 验证成功 获取所有的正确信息
            # {'user': 'assa', 'pwd': 'sadasd', 'email': 'sdasdsad@123.com'}
            print(form.cleaned_data)
            models.UserInfo.objects.create(**form.cleaned_data)
            return HttpResponse("注册成功")
        else:
            # errors默认为html语言可转换为json
            print(form.errors.as_json())
            # 验证失败 显示错误信息
            return render(request, "form_test.html", {'form': form})
        return redirect('/test_form/')
# endregion
