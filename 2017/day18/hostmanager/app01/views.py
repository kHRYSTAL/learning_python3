from django.shortcuts import render, redirect, HttpResponse
from app01 import models


# Create your views here.

def business(request):
    """ 业务线 调用函数"""
    # 获取所有业务线数据 只获取id与caption
    businesses1 = models.Business.objects.all()
    # 没有values的情况
    # 返回QuerySet数据 继承于列表 内部为Business对象
    # [business(id, caption, english),..]

    businesses2 = models.Business.objects.all().values('id', 'caption')
    # 有values情况
    # 返回QuerySet 字典对象列表
    # [{id: xx, caption:xxx}, ...]
    print(businesses2)
    businesses3 = models.Business.objects.all().values_list('id', 'caption')
    # 有values情况
    # 返回QuerySet 元组对象列表
    # [(xx, xxx), ...]
    print(businesses3)
    return render(request, 'business.html',
                  {'businesses1': businesses1, 'businesses2': businesses2, 'businesses3': businesses3})
