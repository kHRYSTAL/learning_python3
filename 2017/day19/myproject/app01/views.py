from django.shortcuts import render, redirect, HttpResponse


# Create your views here.

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

    return render(request, 'tpl4.html', {'msg': msg, 'val1': 3, 'val2': 4, 'val3': 5, 'id': 'id_username', 'class': 'hide'})

