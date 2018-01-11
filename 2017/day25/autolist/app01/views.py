from django.shortcuts import render, HttpResponse
from django.views import View
from app01 import models
import json


class BaseResponse(object):
    def __init__(self):
        self.status = True
        self.data = None
        self.message = None


# Create your views here.

class ServerView(View):
    def get(self, request, *agrs, **kwargs):
        return render(request, 'server.html')


class ServerJsonView(View):
    def get(self, request, *agrs, **kwargs):
        response = BaseResponse()
        try:
            # 获取要显示的列的头
            table_config = [
                {
                    'q': 'hostname',
                    'title': '主机名',
                    'display': 1

                },
                {
                    'q': 'port',
                    'title': '端口',
                    'display': 1
                },
                {
                    'q': 'business_unit_id',
                    'title': '业务线ID',
                    'display': 1
                },
                {
                    'q': 'business_unit__name',  # 双下划线为跨表查询
                    'title': '业务线名称',
                    'display': 1
                },
                {
                    'q': None,
                    'title': '操作',
                    'display': 1
                }
            ]
            # 获取列对应的值

            # region 通过列头的q字段作为数据库查询的值进行查询
            value_list = []

            for item in table_config:
                if item['q']:
                    value_list.append(item['q'])

            # querySet
            data_list = models.Server.objects.values(*value_list)
            # [{}, {}, {},]
            # endregion

            # 将querySet序列化为列表
            data_list = list(data_list)
            print(data_list)

            response.data = {
                'table_config': table_config,
                'data_list': data_list
            }
        except Exception as e:
            response.status = False
            response.message = str(e)
        return HttpResponse(json.dumps(response.__dict__))
