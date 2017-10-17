from django.shortcuts import render, redirect, HttpResponse

# Create your views here.


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

