#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 自定义filter
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: custom_tpl_filter.py
# @time: 17/10/6 下午11:32
from django import template

register = template.Library()


@register.filter
def combine_str(str1, str2):
    return str1 + str2
