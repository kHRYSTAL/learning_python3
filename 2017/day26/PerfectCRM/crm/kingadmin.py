#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: kingadmin.py
# @time: 18/3/26 下午3:05

from crm import models
from kingadmin.base_admin import site, BaseAdmin


class CustomerAdmin(BaseAdmin):
    """默认展现列"""
    list_display = ('id', 'name', 'qq', 'consultant', 'source', 'consult_content', 'status', 'date')
    """过滤器"""
    list_filter = ('source', 'status', 'consultant')
    """搜索"""
    search_fields = ('qq', 'name')
    """是否可编辑"""
    list_editable = ('status',)


site.register(models.Customer, CustomerAdmin)
site.register(models.CourseRecord)
