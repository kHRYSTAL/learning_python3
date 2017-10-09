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
    """ 分页测试 """
    current_page = request.GET.get('p', 1)
    current_page = int(current_page)

    page_obj = Page(current_page, len(LIST), 5, 11)

    # 获取应当给前端显示的item列表
    li = LIST[page_obj.start: page_obj.end]

    page_str = page_obj.generate_page_str('/user_list?p=')
    return render(request, 'user_list.html', {'user_list': li, 'page_str': page_str})


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


def after_login(request):
    # 获取当前已登录用户名
    value = request.COOKIES.get('cookies_username')

    if not value:
        # 如果用户名为空 则跳转到登录页面重新登录
        return redirect('/login/')
    return HttpResponse("Login OK")
# endregion
