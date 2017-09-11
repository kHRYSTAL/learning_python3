from django.shortcuts import render, HttpResponse, redirect


# Create your views here.


# def index(request):
#     return HttpResponse('index')


# def login(request):
#     if request.method == 'GET':
#         return render(request, 'login.html')
#     elif request.method == 'POST':
#         u = request.POST.get('user')
#         p = request.POST.get('pwd')
#         if u == 'matt' and p == '123':  # 用户名密码正确, 返回首页
#             return redirect('/index/')
#         else:  # 不正确render当前页面
#             return render(request, 'login.html')
#     else:
#         # PUT DELETE HEAD OPTION
#         # 其他方式提交 跳转回首页
#         return redirect('/index/')

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        # single_val = request.POST.get('gender')
        # print("获取单选gender", single_val)
        # multi_val = request.POST.getlist('favour')
        # print("获取多选favour", multi_val)
        #
        # multi_city_val = request.POST.getlist('city')
        # print("获取多选city", multi_city_val)
        #
        # file_obj = request.FILES.get('upload_file')
        # if file_obj is not None:
        #     print('获取上传文件', file_obj, type(file_obj))
        #     print('文件名称', file_obj.name)
        #
        #     # 获取上传的文件 保存在服务器
        #     import os
        #     file_path = os.path.join('upload', file_obj.name)
        #     f = open(file_path, mode='wb')
        #     # chunks 是上传文件的块 是一个生成器 需要迭代
        #     for block in file_obj.chunks():
        #         f.write(block)
        #     f.close()
        # else:
        #     print('文件为空')

        # 数据库中获取数据 select * from user where username='x' and password='x';

        return render(request, 'login.html')
    else:
        # PUT DELETE HEAD OPTION
        # 其他方式提交 跳转回首页
        return redirect('/index/')


# def home(request):
#     """fbv function base view"""
#     return HttpResponse('home')

from django.views import View


class Home(View):
    """class base view"""

    def dispatch(self, request, *args, **kwargs):
        # 重写dispatch方法 在父类中 dispatch会通过反射分发执行get或post函数
        # 相当于装饰器的作用
        print('before execute Home class dispatch')
        # 调用父类函数
        result = super(Home, self).dispatch(request, *args, **kwargs)
        print('after execute Home class dispatch')
        return result

    def get(self, request):
        # get请求执行
        print(request.method)
        return render(request, 'home.html')

    def post(self, request):
        # post 请求执行
        print(request.method)
        name = request.POST.get('name')
        print('获取post提交的name:', name)
        return HttpResponse('获取post提交的name:' + name)


USER_DICT = {
    '1': {'name': 'root', 'email': 'root@live.com'},
    '2': {'name': 'khrystal', 'email': 'root@live.com'},
    '3': {'name': 'matt', 'email': 'root@live.com'},
    '4': {'name': 'gloria', 'email': 'root@live.com'},
    '5': {'name': 'pig', 'email': 'root@live.com'},
}

"""
USER_LIST = [
     {'name': 'root', 'email': 'root@live.com'},
     {'name': 'khrystal', 'email': 'root@live.com'},
     {'name': 'matt', 'email': 'root@live.com'},
     {'name': 'gloria', 'email': 'root@live.com'},
     {'name': 'pig', 'email': 'root@live.com'},
]

{% for item in user_list %}
"""


def index(request):
    return render(request, 'index.html', {'user_dict': USER_DICT})


# def detail(request):
#     """获取拼接url中的数据"""
#     # return HttpResponse("detail")
#     nid = None
#     if request.method == "GET":
#         nid = request.GET.get('nid')
#         detail_info = USER_DICT[nid]
#     return render(request, 'detail.html', {'detail_info': detail_info})


def detail(request, nid):
    """获取正则url中的数据
        url: detail-1
        reg: detail-(\d+)
        reg: detail-(P<nid>\d+) 分组正则
        第二个参数是根据urls.py 定义的url正则中的括号包裹的数据返回的
        这里返回1
    """
    detail_info = USER_DICT[nid]
    return render(request, 'detail.html', {'detail_info': detail_info})