#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 自定义模版函数
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: custom_tpl_func.py
# @time: 17/10/5 下午11:48

from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag
def my_simple_time(v1, v2, v3):
    return v1 + v2 + v3


@register.simple_tag
def my_input(id, arg):
    result = "<input type='text' id='%s' class='%s' />" % (id, arg,)
    return mark_safe(result)