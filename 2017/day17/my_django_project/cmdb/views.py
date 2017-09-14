from django.shortcuts import render, HttpResponse, redirect, reverse


# Create your views here.
def cmdb_index(request):
    return render(request, 'cmdb_index.html')


def cmdb_login(request):
    if request.method == 'GET':
        return render(request, 'cmdb_login.html')
    elif request.method == 'POST':
        u = request.POST.get('user')
        p = request.POST.get('pwd')
        obj = models.UserInfo.objects.filter(username=u, password=p).first()  # 获取第一个对象
        count = models.UserInfo.objects.filter(username=u, password=p).count()  # 获取个数
        print(obj)  # None, 不存在用户
        print(count)
        if obj:
            # 通过别名反转获取url
            return redirect(reverse('cmdb-index'))
        else:
            return render(request, 'cmdb_login.html')
    else:
        # PUT DELETE HEAD OPTION
        # 其他方式提交 跳转回首页
        return redirect('/index/')


def cmdb_userinfo(request):
    if request.method == 'POST':
        # Post提交为创建用户
        u = request.POST.get('username')
        p = request.POST.get('password')
        # 创建用户
        models.UserInfo.objects.create(username=u, password=p)
        # 重新以get形式跳转回当前页面 可以使用redirect 状态码为302
        return redirect(request.path_info)
    else:
        user_list = models.UserInfo.objects.all()
        return render(request, 'cmdb_userinfo.html', {'user_list': user_list})


def cmdb_userdetail(request, uid):
    user = models.UserInfo.objects.filter(id=uid).first()
    return render(request, 'cmdb_userdetail.html', {'user': user})


def cmdb_userdelete(request, uid):
    models.UserInfo.objects.filter(id=uid).delete()
    return redirect(reverse('cmdb-userinfo'))


def cmdb_useredit(request, uid):
    if request.method == 'GET':
        obj = models.UserInfo.objects.filter(id=uid).first()
        return render(request, 'cmdb_useredit.html', {'user': obj})
    else:
        u = request.POST.get('username')
        p = request.POST.get('password')
        models.UserInfo.objects.filter(id=uid).update(username=u, password=p)
        return redirect(reverse('cmdb-userinfo'))



def cmdb_usergroup(request):
    return render(request, 'cmdb_usergroup.html')


from app01 import models


def orm(request):
    # 1,增
    # 增加, 创建数据 保存至数据库
    # models.UserInfo.objects.create(
    #     username='root',
    #     password='123'
    # )
    # 或者
    # dict = {'username': 'matt', 'password': '789'}
    # # dict为字典 **dict为将字典数据遍历放置到参数中
    # models.UserInfo.objects.create(**dict)

    # 增加, 创建数据 保存至数据库
    # 实例化一个对象
    # obj = models.UserInfo(username='admin', password='345')
    # # 保存至数据库
    # obj.save()

    # 2, 查
    # 查询所有数据
    # allSelect = models.UserInfo.objects.all()
    # for i in allSelect:
    #     print(i.username)

    # 条件查询
    # whereSelect = models.UserInfo.objects.filter(id=1)
    # for i in whereSelect:
    #     print(i.username)

    # 3, 删
    # 删除所有
    # models.UserInfo.objects.all().delete()
    # 条件删除
    # models.UserInfo.objects.filter(id=4).delete()

    return HttpResponse("orm")
