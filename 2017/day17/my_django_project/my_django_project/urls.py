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
from django.contrib import admin
from app01 import views

urlpatterns = [
    # region app01模块
    url(r'^admin/', admin.site.urls),  # django自动生成的后台管理url
    url(r'^index/', views.index, name='index_alias'),  # 设置别名
    url(r'^login/', views.login),
    url(r'^home/', views.Home.as_view()),
    # 在html中拼接实现url携带数据
    # url(r'^detail/', views.detail),
    # 正则实现url携带数据
    url(r'^detail-(\d+)', views.detail),
    # endregion

    # cmdb模块路由分发模式
    url(r'^cmdb/', include("cmdb.urls"))
]
