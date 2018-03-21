from django.shortcuts import render


# Create your views here.

def acc_login(request):
    """account login"""
    return render(request, "login.html")