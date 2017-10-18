#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: signal_receiver.py
# @time: 17/10/18 下午2:35


from django.core.signals import request_finished
from django.core.signals import request_started
from django.core.signals import got_request_exception

from django.db.models.signals import class_prepared
from django.db.models.signals import pre_init, post_init
from django.db.models.signals import pre_save, post_save
from django.db.models.signals import pre_delete, post_delete
from django.db.models.signals import m2m_changed
from django.db.models.signals import pre_migrate, post_migrate

from django.test.signals import setting_changed
from django.test.signals import template_rendered

from django.db.backends.signals import connection_created


# region 注册方式1
# 接受信号函数
def callback(sender, **kwargs):
    print("pre_init_callback")
    print(sender, kwargs)

# 注册接受数据库对象构造函数触发信号
pre_init.connect(callback)
# endregion

# region 注册方式2
from django.core.signals import request_finished
from django.dispatch import receiver
@receiver(request_finished)
def my_callback(sender, **kwargs):
    print("Request finished!")
# endregion


# region 自定义信号
import django.dispatch

pizza_done = django.dispatch.Signal(providing_args=["toppings", "size"])


def pizza_done_callback(sender, **kwargs):
    print("pizza_done_callback")
    print(sender, kwargs)

pizza_done.connect(callback)
# endregion


