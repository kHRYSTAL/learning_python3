from django import views
from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
from utils.pagination import Page


def index(request):
    # 封装所有用户请求信息
    # print(request.environ)
    # for k, v in request.environ.items():
    #     print(k, v)
    print(request.environ['HTTP_USER_AGENT'])
    return HttpResponse('OK')


# region 母版
# 这些页面只是内容不同 但具有公共的header, css, js 因此可以将公共的部分提取成一个母版供子类使用
def tpl1(request):
    """ 模板继承 母版 """
    u = [1, 2, 3, 4]
    return render(request, 'tpl1.html', {'u': u})


def tpl2(request):
    """ 模板继承 母版 """
    name = 'khrystal'
    return render(request, 'tpl2.html', {'name': name})


def tpl3(request):
    """ 模板继承 母版 """
    status = '已经删除'
    return render(request, 'tpl3.html', {'status': status})


# endregion


# region 自定义模版函数
def tpl4(request):
    """ 自定义模版函数 """
    msg = '自定义模版函数'

    return render(request, 'tpl4.html',
                  {'msg': msg, 'val1': 3, 'val2': 4, 'val3': 5, 'id': 'id_username', 'class': 'hide'})


# endregion


# region 自定义分页
# 测试数据 全局变量
LIST = []
for i in range(109):
    LIST.append(i)


def user_list(request):
    """ cookies 获取测试 """
    # 第二个参数为取不到cookies的默认值
    page_of_count = int(request.COOKIES.get('page_of_count', 10))
    print('cookies', page_of_count)
    """ 分页测试 """
    current_page = request.GET.get('p', 1)
    current_page = int(current_page)

    page_obj = Page(current_page, len(LIST), page_of_count, 11)

    # 获取应当给前端显示的item列表
    li = LIST[page_obj.start: page_obj.end]

    page_str = page_obj.generate_page_str('/user_list?p=')
    return render(request, 'user_list.html', {'user_list': li, 'page_str': page_str, 'page_of_count': page_of_count})


# endregion

# region 用户认证装饰器

def auth(func):
    def wrapper(request, *args, **kwargs):
        username = request.COOKIES.get('cookies_username')
        if not username:
            # 如果cookie中没有用户名 说明未登录 跳转到登录
            return redirect('/login/')
        # 执行被装饰的函数 跳转页面由func自己处理 最后通过wrapper返回
        return func(request, *args, **kwargs)

    return wrapper


# endregion

# region cookies

USER_INFO = {
    'khrystal': {'pwd': '123123'},
    'yyg': {'pwd': '234234'},
}


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        u = request.POST.get('username')
        p = request.POST.get('pwd')
        dic = USER_INFO.get(u)
        if not dic:
            # 查询不到用户数据
            return render(request, 'login.html')
        if dic['pwd'] == p:
            # 查询到用户数据且密码正确
            # 获取到要传递给客户端的数据并setcookies
            res = redirect('/after_login/')
            # 设置cookies

            res.set_cookie('cookies_username', u)
            return res
        else:
            # 密码错误
            return render(request, 'login.html')


@auth
def after_login(request):
    # 获取当前已登录用户名
    # value = request.COOKIES.get('cookies_username')
    #
    # if not value:
    #     # 如果用户名为空 则跳转到登录页面重新登录
    #     return redirect('/login/')
    return HttpResponse("Login OK")

from django.utils.decorators import method_decorator

# 可以直接在类上加装饰器 指明哪个请求方式需要加验证 可以直接加到dispatch上 表明所有请求方式都需要验证
#@method_decorator(auth, name='dispatch')
class Order(views.View):
    """ CBV 用户认证 """
    # @method_decorator(auth)
    # def dispatch(self, request, *args, **kwargs):
    #     """如果全部请求都需要认证 那么直接加到dispatch上就可以"""
    #     return super().dispatch(request, *args, **kwargs)

    @method_decorator(auth)
    def get(self, request):
        username = request.COOKIES.get('cookies_username')
        # if not username:
        #     # 如果cookie中没有用户名 说明未登录 跳转到登录
        #     return redirect('/login/')
        return render(request, 'order.html', {'current_user': username})

    @method_decorator(auth)
    def post(self, request):
        username = request.COOKIES.get('cookies_username')
        # if not username:
        #     # 如果cookie中没有用户名 说明未登录 跳转到登录
        #     return redirect('/login/')
        return render(request, 'order.html', {'current_user': username})


def cookies(request):
    # 获取用户请求时携带的cookies, cookies实际上时一个字典
    val1 = request.COOKIES['cookies_username']
    val2 = request.COOKIES.get('cookies_username')

    # 设置cookies
    response = render(request, 'index.html')
    # response = redirect('index')

    # 默认不加除k-v之外的参数 关闭浏览器后就失效
    response.set_cookie('key', 'value')
    # 超时时间为100秒后 单位为秒 超过这个时间cookies失效 浏览器在超时后删除
    import datetime
    # 获取当前时间
    current_date = datetime.datetime.utcnow()
    current_date = current_date + datetime.timedelta(seconds=100)
    response.set_cookie('key', 'value', max_age=100)  # 最大有效期为100秒 cookies被浏览器访问后触发计时
    response.set_cookie('key', 'value', expires=current_date)  # 失效日期为指定日期到1970.1.1的秒数
    # max_age 与expires 属性都是指定失效时间 max_age已经代替expires 但为了兼容性 两个属性都需要设置

    # 设置加盐加密签名
    response.set_signed_cookie('key', 'value', 'salt')
    # 获取加盐加密签名
    request.get_signed_cookie('key', 'salt')
    return response

# endregion
