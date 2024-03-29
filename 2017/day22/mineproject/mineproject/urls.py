"""mineproject URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from app01 import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/', views.index),
    url(r'^user_list/$', views.user_list),
    url(r'^edit-(\d+)/$', views.user_edit),
    url(r'ajax_test/$', views.ajax_test),
    url(r'ajax_json/$', views.ajax_json),
    url(r'upload/$', views.upload),
    url(r'upload_file/$', views.upload_file),
    url(r'image_code/$', views.image_code),
    url(r'check_code/$', views.check_code),  # 生成验证码图片url
    url(r'kind/$', views.kind),
    url(r'kind_upload_img/$', views.kind_upload_img),
    url(r'file_manager/$', views.file_manager),
    url(r'volvo/$', views.volvo),
    url(r'redirect_wechat', views.redirect_wechat),

]
