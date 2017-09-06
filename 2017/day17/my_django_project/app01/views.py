from django.shortcuts import render, HttpResponse, redirect


# Create your views here.


def index(request):
    return HttpResponse('index')


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
        single_val = request.POST.get('gender')
        print("获取单选gender", single_val)
        multi_val = request.POST.getlist('favour')
        print("获取多选favour", multi_val)

        multi_city_val = request.POST.getlist('city')
        print("获取多选city", multi_city_val)

        file_obj = request.FILES.get('upload_file')
        if file_obj is not None:
            print('获取上传文件', file_obj, type(file_obj))
            print('文件名称', file_obj.name)

            # 获取上传的文件 保存在服务器
            import os
            file_path = os.path.join('upload', file_obj.name)
            f = open(file_path, mode='wb')
            # chunks 是上传文件的块 是一个生成器 需要迭代
            for block in file_obj.chunks():
                f.write(block)
            f.close()
        else:
            print('文件为空')

        return render(request, 'login.html')
    else:
        # PUT DELETE HEAD OPTION
        # 其他方式提交 跳转回首页
        return redirect('/index/')



