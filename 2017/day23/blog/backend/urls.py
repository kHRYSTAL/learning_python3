#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: urls.py
# @time: 17/12/3 下午10:47


from django.conf.urls import url
from .views import user

urlpatterns = [
    url(r'^base-info.html$', user.base_info),
    url(r'^tag.html$', user.tag),
    url(r'^category.html$', user.category),
    url(r'^article.html$', user.article),
    url(r'^add-article.html$', user.add_article),
    url(r'^edit-article-(\d+).html$', user.edit_article),
]
