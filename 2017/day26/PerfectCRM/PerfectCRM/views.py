from django.shortcuts import render, redirect
# 引入django内部的认证 因为userprofile表与user表是一对一关系
from django.contrib.auth import authenticate, login, logout
# django内置装饰器 用于校验用户是否已经登录 如果用户未登录 需要跳转至login页面
# 该装饰器表明请求某个函数时login是必须的
from django.contrib.auth.decorators import login_required


# Create your views here.

def acc_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)  # 认证
        # 自带的认证 当用户认证成功后 会将user直接设置到session中 可以直接通过request.user在前后端调用 不需要我们进行任何操作
        print(user.crm_user.name)
        if user:
            login(request, user)  # 登录, 此时会把user设置到session和request中
            # 如果返回用户对象, 说明认证成功, None为没认证成功
            # auth pass
            return redirect("/crm")
    """account login"""
    return render(request, "login.html")

@login_required
def acc_logout(request):
    # 执行django的user退出 此时会退出并移除session中的user
    logout(request)
    return redirect("/login")
