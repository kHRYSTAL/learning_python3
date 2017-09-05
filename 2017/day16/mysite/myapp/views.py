from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.
# 这里的view 指代control
from django.shortcuts import HttpResponse


def login(request):
    """
    根据提交方式的不同 进行不同的处理, 默认是get 提交表单是post
    request包含客户端发给服务器的所有信息
    """
    # 获取用户的提交方式 GET 或 POST
    print(request.method)
    error_msg = ""
    if request.method == "POST":
        # 获取POST请求中的数据 POST为字典
        uname = request.POST.get('uname', None)
        pwd = request.POST.get('pwd', None)
        print(uname, pwd)

        # 验证用户名是否正确
        if uname == 'root' and pwd == '123':
            # 如果正确 重定向到baidu
            return redirect('http://www.baidu.com')
        else:
            error_msg = "用户名密码不匹配"
            # # 用户名密码不匹配 替换模版文件对应字符串 可以与最后的return方法合并
            # return render(request, 'login.html', {'error_msg': '用户名密码不匹配'})
    # f = open('template/login.html', 'r', encoding='utf-8')
    # data = f.read()
    # f.close()
    # return HttpResponse(data)
    # 上述代码可以使用render一行解决 去模版文件夹寻找模版文件
    return render(request, 'login.html', {'error_msg': error_msg})


def home(request):
    return HttpResponse('<h1>hello</h1>')
