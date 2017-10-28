#!/usr/bin/env python
# -*- coding:utf-8 -*-

from django.shortcuts import render, HttpResponse, redirect
from django import forms
from django.forms import fields

from app01 import models

"""
备份文件 使用form做验证功能
"""


# Create your views here.

class UserInfoForm(forms.Form):
    username = fields.CharField(max_length=32)
    email = fields.EmailField()
    user_type = fields.ChoiceField(
        choices=models.UserType.objects.values_list('id', 'caption')
    )

    def __init__(self, *args, **kwargs):
        super(UserInfoForm, self).__init__(*args, **kwargs)
        # 保证每次调用这个类初始化时 choices都更新保证与数据库时时同步
        self.fields['user_type'].choices = models.UserType.objects.values_list('id', 'caption')


'''
由于UserInfoForm 与 model中的userinfo字段是一样的可以使用ModelForm 把验证与数据库存储完全用
一个类解决
'''


class UserInfoModelForm(forms.ModelForm):
    class Meta:
        # 指定数据库的类
        model = models.UserInfo
        fields = '__all__'


def index(request):
    if request.method == 'GET':
        form = UserInfoModelForm()
        return render(request, 'index.html', {'form': form})

    elif request.method == 'POST':
        form = UserInfoModelForm(request.POST)
        res = form.is_valid()
        # if res:
        #     # 验证成功 获取所有的正确信息
        #     print(form.cleaned_data)
        #     models.UserInfo.objects.create(**form.cleaned_data)
        #     # models.UserInfo.objects.filter(id=1).update(**form.cleaned_data)
        #     return HttpResponse("注册成功")
        # else:
        #     # errors默认为html语言可转换为json
        #     print(form.errors.as_json())
        #     # 验证失败 显示错误信息
        #     return render(request, "index.html", {'form': form})
        return redirect('/index/')
