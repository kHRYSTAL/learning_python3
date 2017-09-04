from django.shortcuts import render

# Create your views here.
# 这里的view 指代control
from django.shortcuts import HttpResponse


def home(request):
    return HttpResponse('<h1>hello</h1>')