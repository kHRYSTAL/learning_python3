#!/usr/bin/env python
# -*- coding:utf-8 -*-

from django.shortcuts import render, HttpResponse, redirect
from django import forms
from django.forms import fields
from django.forms import widgets as Fwidgets

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
    # 定义额外字段 记住登录状态 与数据库表无关
    is_remember = fields.CharField(
        widget=Fwidgets.CheckboxInput()
    )

    class Meta:
        # 指定数据库的类
        model = models.UserInfo
        fields = '__all__'

    # def clean_username(self):
    #     """ clean_[field] """
    #     """
    #     username字段验证与转换
    #     如: username中不能传递特殊字符和表情
    #     可以在这个函数内过滤
    #     """
    #     old_val = self.cleaned_data['username']
    #     return "..."


def index(request):
    if request.method == 'GET':
        form = UserInfoModelForm()
        return render(request, 'index.html', {'form': form})

    elif request.method == 'POST':
        form = UserInfoModelForm(request.POST)
        res = form.is_valid()
        if res:
            # 使用modelform可直接保存至数据库 比form获取cleaned_data再保存更简单
            # 支持多对多的表存储
            form.save()
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


def user_list(request):
    # selected_related 不支持多对多的查询优化
    li = models.UserInfo.objects.select_related('user_type').all()
    return render(request, 'user_list.html', {'li': li})


def user_edit(request, nid):
    # 获取当前id对应的用户信息
    # 显示用户已经存在的数据至input
    if request.method == 'GET':
        user_obj = models.UserInfo.objects.filter(id=nid).first()
        # 页面显示的表单  # 将user_obj 设置为表单中的默认数据
        mf = UserInfoModelForm(instance=user_obj)
        return render(request, 'user_edit.html', {'mf': mf})
    elif request.method == 'POST':  # 提交数据
        user_obj = models.UserInfo.objects.filter(id=nid).first()
        # 如果验证成功 需要update, 只使用save()是创建 因此也需要设置指定的默认数据
        mf = UserInfoModelForm(request.POST, instance=user_obj)
        if mf.is_valid():
            print(mf.cleaned_data.get('is_remember')) # 保存到session
            mf.save()
        else:
            print(mf.errors.as_json())
        return render(request, 'user_edit.html', {'mf': mf})
