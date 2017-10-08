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


# region 这些页面只是内容不同 但具有公共的header, css, js 因此可以将公共的部分提取成一个母版供子类使用
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


def tpl4(request):
    """ 自定义模版函数 """
    msg = '自定义模版函数'

    return render(request, 'tpl4.html',
                  {'msg': msg, 'val1': 3, 'val2': 4, 'val3': 5, 'id': 'id_username', 'class': 'hide'})


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
