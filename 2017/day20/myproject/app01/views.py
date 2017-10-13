from django.shortcuts import render, redirect, HttpResponse

# Create your views here.


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        if user == 'root' and pwd == '123':
            # 生成随机字符串
            # 写到用户浏览器cookie
            # 保存至session中 key为随机字符串 value为用户相关信息
            # django 会自动执行以上所有操作 只需要一行代码
            request.session['username'] = user
            request.session['is_login'] = True
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
