#!/usr/bin/env python
# -*- coding:utf-8 -*-

from django.shortcuts import render, HttpResponse, redirect, render_to_response
from django import forms
from django.forms import fields
from django.forms import widgets as Fwidgets
from io import BytesIO

from app01 import models
from utils.check_code import create_validate_code

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


def redirect_wechat(request):
    return render(request, 'test.html')


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
            print(mf.cleaned_data.get('is_remember'))  # 保存到session
            mf.save()
        else:
            print(mf.errors.as_json())
        return render(request, 'user_edit.html', {'mf': mf})


def ajax_test(request):
    return render(request, 'ajax_test.html')


def ajax_json(request):
    import time
    time.sleep(3)
    print(request.POST)
    ret = {'status': True, 'data': None}
    import json
    # return HttpResponse(json.dumps(ret), status=404, reason="找不到页面")  # 自定义状态码
    return HttpResponse(json.dumps(ret))


def upload(request):
    return render(request, 'upload.html')


def upload_file(request):
    """ 用于接收上传的值和文件 """
    username = request.POST.get('username')
    file = request.FILES.get('file')

    import os
    img_path = os.path.join('static/image', username + file.name)
    print(username, file)

    with open(img_path, 'wb') as f:
        for item in file.chunks():
            f.write(item)

    ret = {'status': True, 'data': img_path}
    import json
    return HttpResponse(json.dumps(ret))


def check_code(request):
    """
    验证码
    :param request:
    :return:
    """
    # stream = BytesIO()
    # img, code = create_validate_code()
    # img.save(stream, 'PNG')
    # request.session['CheckCode'] = code
    # return HttpResponse(stream.getvalue())

    # data = open('static/imgs/avatar/20130809170025.png','rb').read()
    # return HttpResponse(data)

    # 1. 创建一张图片 pip3 install Pillow
    # 2. 在图片中写入随机字符串
    # obj = object()
    # 3. 将图片写入到制定文件
    # 4. 打开制定目录文件，读取内容
    # 5. HttpResponse(data)

    stream = BytesIO()
    img, code = create_validate_code()
    img.save(stream, 'PNG')
    request.session['CheckCode'] = code
    return HttpResponse(stream.getvalue())


def image_code(request):
    """
    登陆
    :param request:
    :return:
    """
    # if request.method == "POST":
    #     if request.session['CheckCode'].upper() == request.POST.get('check_code').upper():
    #         pass
    #     else:
    #         print('验证码错误')
    if request.method == 'POST':
        code = request.POST.get('check_code')
        if code.upper() == request.session['CheckCode'].upper():
            print('验证码正确')
        else:
            print('验证码错误')
    return render(request, 'image_code.html')


def kind(request):
    return render(request, 'kind.html')


def kind_upload_img(request):
    file_dir = request.GET.get('dir')
    if file_dir == 'image':
        print("dir is:", file_dir)
    file = request.FILES.get('imgFile')
    import os
    import datetime
    filename = str(datetime.datetime.now().timestamp()) + '.jpg'
    img_path = os.path.join('static/image', filename)

    with open(img_path, 'wb') as f:
        for item in file.chunks():
            f.write(item)

    import json
    dic = {
        'error': 0,  # 0代表正确 1代表错误
        'url': "/" + img_path,
        'message': "success"
    }
    return HttpResponse(json.dumps(dic))


import os
import json
import time


def file_manager(request):
    """
    文件管理
    :param request:
    :return:
    kind 文件空间需要的格式
    {
        moveup_dir_path: 上一级文件夹路径
        current_dir_path: 当前文件夹路径
        current_url: 图片或其他可预览文件的前缀 在settings.py 配置 这里设置的是/static/
        当前文件夹下的内容 默认每一个文件都是一个字典
        file_list:[
            {
                'is_dir': // 是否为文件夹
                'has_file': // 里面是否有文件,
                'filesize': // 文件大小 文件夹可以设置为0 也可以设置内部文件大小
                'dir_path': // 路径
                'is_photo': // 是否是图片
                'filetype': // 文件类型
                'filename': // 文件名
                'datetime': // 创建时间
            }
        ]
    }
    """
    dic = {}
    root_path = '/Users/kHRYSTAL/PycharmProjects/learning_python3/2017/day22/mineproject/static/'  # 用户可以查看文件路径的根
    static_root_path = '/static/'
    request_path = request.GET.get('path')
    if request_path:
        abs_current_dir_path = os.path.join(root_path, request_path)
        move_up_dir_path = os.path.dirname(request_path.rstrip('/'))
        dic['moveup_dir_path'] = move_up_dir_path + '/' if move_up_dir_path else move_up_dir_path

    else:
        abs_current_dir_path = root_path
        dic['moveup_dir_path'] = ''

    dic['current_dir_path'] = request_path
    dic['current_url'] = os.path.join(static_root_path, request_path)

    file_list = []
    for item in os.listdir(abs_current_dir_path):
        abs_item_path = os.path.join(abs_current_dir_path, item)
        a, exts = os.path.splitext(item)
        is_dir = os.path.isdir(abs_item_path)
        if is_dir:
            temp = {
                'is_dir': True,
                'has_file': True,
                'filesize': 0,
                'dir_path': '',
                'is_photo': False,
                'filetype': '',
                'filename': item,
                'datetime': time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(os.path.getctime(abs_item_path)))
            }
        else:
            temp = {
                'is_dir': False,
                'has_file': False,
                'filesize': os.stat(abs_item_path).st_size,
                'dir_path': '',
                'is_photo': True if exts.lower() in ['.jpg', '.png', '.jpeg'] else False,
                'filetype': exts.lower().strip('.'),
                'filename': item,
                'datetime': time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(os.path.getctime(abs_item_path)))
            }

        file_list.append(temp)
    dic['file_list'] = file_list
    return HttpResponse(json.dumps(dic))


def volvo(request):
    return render(request, 'woerwoxcx.html')
