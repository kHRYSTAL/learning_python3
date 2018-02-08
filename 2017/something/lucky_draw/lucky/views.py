from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html')


def users(request):
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        pass
