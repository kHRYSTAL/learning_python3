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
def filter_all(arg_dict, types):
    # 0 为文章类型 1为文章标签分类
    """
    {% if arg_dict.article_type_id == 0 %}
                <a class="active" href="/article-0-{{arg_dict.category_id}}.html">全部</a>
    {% else %}
        <a href="/article-0-{{arg_dict.category_id}}.html">全部</a>
    {% endif %}

    {% for row in article_type_list %}
        {% if row.id == arg_dict.article_type_id %}
        <a class="active" href="/article-{{row.id}}-{{arg_dict.category_id}}.html">{{row.caption}}</a>
        {% else %}
        <a href="/article-{{row.id}}-{{arg_dict.category_id}}.html">{{row.caption}}</a>
        {% endif %}
    {%endfor%}
    """
    ret = ""
    if types == 0:
        if arg_dict['article_type_id'] == 0:
            ret = '<a class="active" href="/article-0-%s.html">全部</a>' % arg_dict['category_id']
        else:
            ret = '<a href="/article-0-%s.html">全部</a>' % arg_dict['category_id']
    elif types == 1:
        if arg_dict['category_id'] == 0:
            ret = '<a class="active" href="/article-%s-0.html">全部</a>' % arg_dict['article_type_id']
        else:
            ret = '<a href="/article-%s-0.html">全部</a>' % arg_dict['article_type_id']

    return mark_safe(ret)


@register.simple_tag
def filter_other(arg_dict, list_arr, types):
    # # 0 为文章类型 1为文章标签分类
    # list arr 可能为文章类型列表或标签列表
    """
     {% for row in article_type_list %}
        {% if row.id == arg_dict.article_type_id %}
        <a class="active" href="/article-{{row.id}}-{{arg_dict.category_id}}.html">{{row.caption}}</a>
        {% else %}
        <a href="/article-{{row.id}}-{{arg_dict.category_id}}.html">{{row.caption}}</a>
        {% endif %}
    {%endfor%}
    """
    ret = ""
    if types == 0:
        for row in list_arr:
            if row.id == arg_dict['article_type_id']:
                ret += '<a class="active" href="/article-%s-%s.html">%s</a>' % (
                row.id, arg_dict['category_id'], row.caption)
            else:
                ret += '<a href="/article-%s-%s.html">%s</a>' % (row.id, arg_dict['category_id'], row.caption)
    elif types == 1:
        for row in list_arr:
            if row.id == arg_dict['category_id']:
                ret += '<a class="active" href="/article-%s-%s.html">%s</a>' % (
                arg_dict['article_type_id'], row.id, row.caption)
            else:
                ret += '<a href="/article-%s-%s.html">%s</a>' % (arg_dict['article_type_id'], row.id, row.caption)
    return mark_safe(ret)
