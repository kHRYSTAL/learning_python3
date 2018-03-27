from django.shortcuts import render
from django import conf

from kingadmin import app_config
from kingadmin.base_admin import site

# Create your views here.
# 找到settings文件
# print("dj conf:", conf.settings)


def app_index(request):
    """从settings找到所有的app
        再从app中找到app下所有的数据库表
    """
    print("register_sites", site.registered_sites)
    return render(request, 'kingadmin/app_index.html')
