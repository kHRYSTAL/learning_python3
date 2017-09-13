"""my_django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from cmdb import views

urlpatterns = [


    # cmdb模块路由分发模式
    # url 为 cmdb/login
    url(r'^login/', views.cmdb_login, name='cmdb-login'),
    url(r'^index/', views.cmdb_index, name='cmdb-index'),
    url(r'^user_info/', views.cmdb_userinfo, name='cmdb-userinfo'),
    url(r'^user_group/', views.cmdb_usergroup, name='cmdb-usergroup'),
    url(r'^userdetail-(?P<uid>\d+)', views.cmdb_userdetail, name='cmdb-userdetail'),
    # orm 测试
    url(r'^orm/', views.orm)
]