from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from App2.models import DatetimeTest, Dog


def index(request):
    return HttpResponse('这是App2的首页')


def addDatetime(request):
    d = DatetimeTest()
    d.save()
    return HttpResponse('日期添加成功')


def loadStatic(request):
    return render(request, 'loadStatic.html')
