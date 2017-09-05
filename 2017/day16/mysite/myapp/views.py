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
            # 如果正确 重定向到 /home path
            return redirect('/home')
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


# region 假数据
USER_LIST = [
    {'username': 'khrystal', 'email': '723526676@qq.com', 'gender': '男'}
]

# for i in range(20):
#     temp = {'username': 'khrystal' + str(i), 'email': '723526676@qq.com', 'gender': '男'}
#     USER_LIST.append(temp)

# endregion


def home(request):
    """
    管理后台主页 将假数据传递给home.html 在html中遍历列表填充
    如果为post请求 说明该页面点击添加user进行的提交 将数据添加到USER_LIST 重新传递html给用户
    """
    if request.method == 'POST':
        # 获取用户提交的数据
        username = request.POST.get('username')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        addUser = {'username': username, 'email': email, 'gender': gender}
        USER_LIST.append(addUser)
    return render(request, 'home.html', {'user_list': USER_LIST})
