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
from django.shortcuts import HttpResponse


class RowOne(MiddlewareMixin):

    def process_request(self, request):
        """拦截请求"""
        print("RowOne MiddleWare reuqest")

    def process_view(self, request, view_func, view_func_args, view_func_kwargs):
        print("RowOne Middleware process view")

    def process_response(self, request, response):
        print("RowOne MiddleWare response")
        return response

    def process_exception(self, request, exception):
        if isinstance(exception, ValueError):
            print("RowOne MiddleWare handle exception")
            return HttpResponse("RowOne MiddleWare Exception")

    def process_template_response(self, request, response):
        print("RowOne Middle handle template response")
        return response



class RowTwo(MiddlewareMixin):

    def process_request(self, request):
        print("RowTwo MiddleWare request")

    def process_view(self, request, view_func, view_func_args, view_func_kwargs):
        print("RowTwo Middleware process view")

    def process_response(self, request, response):
        print("RowTwo MiddleWare response")
        return response

    def process_exception(self, request, exception):
        print("RowTwo MiddleWare handle exception")

    def process_template_response(self, request, response):
        print("RowTwo Middleware handle template response")
        return response


class RowThree(MiddlewareMixin):

    def process_request(self, request):
        print("RowThree MiddleWare request")

    def process_view(self, request, view_func, view_func_args, view_func_kwargs):
        print("RowThree Middleware process view")

    def process_response(self, request, response):
        print("RowThree MiddleWare response")
        return response

    def process_exception(self, request, exception):
        print("RowThree MiddleWare handle exception")

    def process_template_response(self, request, response):
        print("RowThree Middleware handle template response")
        return response
