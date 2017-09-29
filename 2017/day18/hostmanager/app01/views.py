from django.shortcuts import render, redirect, HttpResponse
from app01 import models


# Create your views here.

def business(request):
    """ 业务线 调用函数"""
    # 获取所有业务线数据 只获取id与caption
    businesses1 = models.Business.objects.all()
    # 没有values的情况
    # 返回QuerySet数据 继承于列表 内部为Business对象
    # [business(id, caption, english),..]

    businesses2 = models.Business.objects.all().values('id', 'caption')
    # 有values情况
    # 返回QuerySet 字典对象列表
    # [{id: xx, caption:xxx}, ...]
    print(businesses2)
    businesses3 = models.Business.objects.all().values_list('id', 'caption')
    # 有values情况
    # 返回QuerySet 元组对象列表
    # [(xx, xxx), ...]
    print(businesses3)
    return render(request, 'business.html',
                  {'businesses1': businesses1, 'businesses2': businesses2, 'businesses3': businesses3})


def host(request):
    if request.method == 'GET':
        hosts1 = models.Host.objects.all()
        # 获取nid > 0 的主机列表
        # hosts = models.Host.objects.filter(nid__gt=0)

        # 获取对应字段列表, 内部对象为字典
        hosts2 = models.Host.objects.filter(nid__gt=0).values('nid', 'ip', 'hostname', 'port', 'business_id',
                                                              'business__caption')

        businesses1 = models.Business.objects.all()
        return render(request, 'host.html', {'hosts1': hosts1, 'hosts2': hosts2, 'businesses': businesses1})
    elif request.method == 'POST':
        hostname = request.POST.get('hostname')
        ip = request.POST.get('ip')
        port = request.POST.get('port')
        business_id = request.POST.get('business_id')
        models.Host.objects.create(
            hostname=hostname,
            ip=ip,
            port=port,
            business_id=business_id,
        )
        return redirect('/host')


def test_ajax(request):
    # 返回结果至h5
    ret = {'status': True, 'error': None, 'data': None}

    try:
        hostname = request.POST.get('hostname')
        ip = request.POST.get('ip')
        port = request.POST.get('port')
        business_id = request.POST.get('business_id')
        print(hostname, len(hostname))
        if hostname and len(hostname) > 5:
            models.Host.objects.create(
                hostname=hostname,
                ip=ip,
                port=port,
                business_id=business_id,
            )
            # return HttpResponse('OK')
            ret['status'] = True
        else:
            # return HttpResponse("太短了")
            ret['status'] = False
            ret['error'] = '太短了'
    except Exception as e:
            ret['status'] = False
            ret['error'] = '服务器出错了'
    finally:
        import json
        # 序列化为字符串传给客户端
        return HttpResponse(json.dumps(ret))


def test_ajax_edit(request):
    # 返回结果至h5
    ret = {'status': True, 'error': None, 'data': None}

    try:
        nid = request.POST.get('nid')
        hostname = request.POST.get('hostname')
        ip = request.POST.get('ip')
        port = request.POST.get('port')
        business_id = request.POST.get('business_id')
        models.Host.objects.filter(nid=nid).update(
            hostname=hostname,
            ip=ip,
            port=port,
            business_id=business_id
        )
        ret['status'] = True
    except Exception as e:
        ret['status'] = False
        ret['error'] = '服务器出错了'
    finally:
        import json
        # 序列化为字符串传给客户端
        return HttpResponse(json.dumps(ret))


def app(request):
    appList = models.Application.objects.all()
    for app in appList:
        print(app.name, app.relation.all())
    return render(request, 'app.html', {'appList': appList})
