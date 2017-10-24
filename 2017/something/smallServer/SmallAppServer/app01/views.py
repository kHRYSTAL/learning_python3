from django.shortcuts import render, HttpResponse
# Create your views here.
import requests


def login(request):
    if request.method == 'GET':
        appid = request.GET.get('appid', 'appid')
        secret = request.GET.get('secret', 'secret')
        js_code = request.GET.get('js_code', 'js_code')
        print(appid, secret, js_code)
        grant_type = "authorization_code"
        resp = requests.get("https://api.weixin.qq.com/sns/jscode2session",
                            params={'appid': appid,
                                    'secret': secret,
                                    'js_code': js_code,
                                    'grant_type': grant_type})
        print(resp.text)
        return HttpResponse(resp.text)
    else:
        import json
        error_data = {"errorcode": -200, "errmsg": "请求方式错误"}
        print(error_data)
        return HttpResponse(json.dumps(error_data))


def index(request):
    if request.method == 'GET':
        resp = requests.get("https://api.weixin.qq.com/sns/jscode2session",
                            params={'appid': 'appid',
                                    'secret': 'secret',
                                    'js_code': 'js_code',
                                    'grant_type': 'grant_type'})
    print(resp.text)
    return HttpResponse(resp.text)
