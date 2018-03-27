#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: base_admin.py
# @time: 18/3/26 下午3:13

"""

sites = {
    'crm': {
        'customers': CustomerAdmin,
        'customerfollowup': CustomerFollowUPAdmin,
    }
}
"""

"""
获取某个model的所在的app的name
models.Customer._meta.app_label
获取model的表名
models.Customer._meta.model_name
"""


class AdminRegisterException(Exception):
    def __init__(self, msg):
        self.message = msg


class BaseAdmin(object):
    """ Admin class 基类 声明字段名 在register中实际上就是去获取这些字段下的值去进行控制显示的 """
    list_display = ()
    list_filter = ()
    search_filter = ()
    list_editable = ()


class AdminSite(object):
    def __init__(self):
        self.registered_sites = {}

    def register(self, model, admin_class=None):
        """
        :param model:  DTO
        :param admin_class: adminClass 控制前端显示列 过滤等等
        :return:
        """
        """ 实现自定义admin, 实现自定义admin.register方法 """
        # app名
        app_name = model._meta.app_label
        # table名
        model_name = model._meta.model_name
        # 初始化app字典
        if app_name not in self.registered_sites:
            self.registered_sites[app_name] = {}
        # 判断model是否注册到app中
        if model_name in self.registered_sites[app_name]:
            raise AdminRegisterException("app [%s] model [%s] has already registered!" % (app_name, model_name))

        if not admin_class:
            # use base_admin
            admin_class = BaseAdmin
        # app字典下表名与adminClass映射
        self.registered_sites[app_name][model_name] = admin_class

site = AdminSite()
