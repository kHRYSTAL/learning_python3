#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: idc_service.py
# @time: 18/1/15 上午11:20


class BaseService(object):

    def __init__(self, tableConfig, conditionConfig):
        self.table_config = tableConfig
        self.condition_config = conditionConfig


class IDCService(BaseService):
    def __init__(self):
        # 过滤器配置 condition_type 为输入或可选择
        condition_config = [
            {'name': 'cabinet_num', 'text': '机柜号', 'condition_type': 'input'},
            # global_name 指代内存中全局变量的字段
            {'name': 'device_type_id', 'text': '资产类型', 'condition_type': 'select', 'global_name': 'device_type_list'},
            {'name': 'device_status_id', 'text': '资产类型', 'condition_type': 'select',
             'global_name': 'device_status_list'}
        ]
        table_config = [
            {
                'q': 'id',
                'title': None,
                'display': 0,
                'text': {}
            },
            {
                'q': 'name',
                'title': '机房',
                'display': 1,
                'text': {'content': '{m}', 'kwargs': {'m': '@name'}},  # 自定义显示内容
                'attr': {'k1': '@name', 'k2': 'v2'}  # 自定义html属性
            },
            {
                'q': 'floor',
                'title': '楼层',
                'display': 1,
                'text': {'content': '{m}', 'kwargs': {'m': '@floor'}},
                'attr': {'k1': '@floor', 'k2': 'v2'}
            },
            {
                'q': None,
                'title': '操作',
                'display': 1,
                'text': {'content': '<a href="/xxx-{nid}.html">查看详细</a>', 'kwargs': {'nid': "@id"}},
                'attr': {'k1': '@id', 'k2': 'v2'}
            }
        ]

        # 调用父类方法
        super(IDCService, self).__init__(table_config, condition_config)

    def fetch_idc(self, request):
        """ 返回baseResponse """
        from app01.views import BaseResponse
        response = BaseResponse()
        try:
            # 根据搜索条件显示内容
            response.data = {
                'table_config': self.table_config,
                'condition_config': self.condition_config
            }
        except Exception as e:
            response.status = False
        return response
