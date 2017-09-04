from django.shortcuts import render

# Create your views here.
# 这里的view 指代control
from django.shortcuts import HttpResponse


def login(request):
    # f = open('template/login.html', 'r', encoding='utf-8')
    # data = f.read()
    # f.close()
    # return HttpResponse(data)
    # 上述代码可以使用render一行解决 去模版文件夹寻找模版文件
    return render(request, 'login.html')


def home(request):
    return HttpResponse('<h1>hello</h1>')
