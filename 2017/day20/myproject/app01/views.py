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


class MyForm(forms.Form):
    """ 指定客户端发送的表单提取的字段 表单的name必须与变量名相同"""
    user = forms.CharField()
    pwd = forms.CharField()
    email = forms.EmailField()


def test_form(request):
    if request.method == 'GET':
        return render(request, "form_test.html")
    elif request.method == 'POST':
        # 获取用户所有的数据
        form = MyForm(request.POST)
        # 每条数据请求的验证是否通过 res为boolean
        res = form.is_valid()
        print(res)
        if res:
            # 验证成功 获取所有的正确信息
            print(form.cleaned_data)
        else:
            # 验证失败 显示错误信息
            print(form.errors.as_json())
        return redirect('/test_form/')
# endregion
