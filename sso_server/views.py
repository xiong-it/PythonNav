# coding=utf-8

from django.shortcuts import render
from sso_server.models import *

#################

def index(request):
    gonggao = notice.objects.all().order_by('-date')[0]
    fenlei = classify.objects.all().order_by('sort')
    return render(request, 'index.html', {'fenlei': fenlei, 'index': 'index','gonggao':gonggao})



