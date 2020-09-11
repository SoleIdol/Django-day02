from django.http import HttpResponse


def index(request):
    return HttpResponse('<h1>欢迎来到首页！</h1>')
