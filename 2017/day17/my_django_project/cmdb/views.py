from django.shortcuts import render, HttpResponse


# Create your views here.

def cmdb_login(request):
    return HttpResponse('CMDB Login\n use router dispatch')
