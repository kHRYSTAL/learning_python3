#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 中间件
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: m1.py
# @time: 17/10/16 下午5:20
from django.utils.deprecation import MiddlewareMixin


class RowOne(MiddlewareMixin):

    def process_request(self, request):
        """拦截请求"""
        print("RowOne MiddleWare")

    def process_response(self, request, response):
        print("RowOne MiddleWare response")
        return response


class RowTwo(MiddlewareMixin):

    def process_request(self, request):
        print("RowTwo MiddleWare")

    def process_response(self, request, response):
        print("RowTwo MiddleWare response")
        return response


class RowThree(MiddlewareMixin):

    def process_request(self, request):
        print("RowThree MiddleWare request")

    def process_response(self, request, response):
        print("RowThree MiddleWare response")
        return response