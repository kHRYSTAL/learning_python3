from django.shortcuts import render, HttpResponse, redirect


# Create your views here.

def cmdb_login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        return render(request, 'login.html')
    else:
        # PUT DELETE HEAD OPTION
        # 其他方式提交 跳转回首页
        return redirect('/index/')


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
