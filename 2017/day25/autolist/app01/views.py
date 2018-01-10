from django.shortcuts import render, HttpResponse
from django.views import View
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
            # 获取要显示的列
            table_config = [
                {
                    'title': '主机名',
                    'display': 1

                },
                {
                    'title': '端口',
                    'display': 1
                }
            ]
            response.data = {
                'table_config': table_config,
            }
        except Exception as e:
            response.status = False
            response.message = str(e)
        print(json.dumps(response.__dict__))
        return HttpResponse(json.dumps(response.__dict__))
