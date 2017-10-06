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
    start = (current_page - 1) * 10
    end = current_page * 10
    # 获取应当给前端显示的item列表
    li = LIST[start: end]
    # 每页10条 求总页数和余数 如果余数大于0 则总页数需要加1
    page_count, remainder = divmod(len(LIST), 10)  # 求商和余数

    if remainder:
        page_count += 1

    # 计算输出给前端的标签字符串
    page_str = ""
    for i in range(1, page_count+1):
        page_str += '<a class="page %s" href="/user_list?p=%s">%s</a>' % ("active" if i == current_page else "", i, i)

    # 向django表明这段注入的标签字符串是安全的 可以正常显示
    from django.utils.safestring import mark_safe
    page_str = mark_safe(page_str)
    return render(request, 'user_list.html', {'user_list': li, 'page_str': page_str})
