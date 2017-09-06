from django.shortcuts import render, HttpResponse, redirect


# Create your views here.


def index(request):
    return HttpResponse('index')


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        u = request.POST.get('user')
        p = request.POST.get('pwd')
        if u == 'matt' and p == '123':  # 用户名密码正确, 返回首页
            return redirect('/index/')
        else:  # 不正确render当前页面
            return render(request, 'login.html')
    else:
        # PUT DELETE HEAD OPTION
        # 其他方式提交 跳转回首页
        return redirect('/index/')
