from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def dashboard(request):
    """ crm首页  用户必须是登录状态 否则跳转至/login
        装饰器默认跳转到 account/login/ 如果url不同 需要修改settings.py 新增LOGIN_URL = "/login/" 指定path与urls.py对应
    """
    return render(request, "crm/dashboard.html")
