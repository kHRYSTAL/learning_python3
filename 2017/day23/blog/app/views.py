from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'index.html')


def startWechat(request):
    return render(request, 'redirect.html')
