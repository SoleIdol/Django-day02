from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from App1.models import Student, Grade


def index(request):
    return HttpResponse('<h3>这是APP1的主页！</h3>')


def foods(request):
    content = {
        'name': '小王',
        'age': 28,
        'gender': '男',
        'foods': ['剁椒鱼头', '糖醋里脊', '干瘪豆角', '红烧排骨']
    }
    
    return render(request, 'foods.html', context=content)


def addStudent(request):
    s = Student()
    s.s_name = '小王'
    s.age = 24
    s.save()
    
    return HttpResponse('添加成功')


def selectStudent(request):
    s = Student.objects.get(pk=4)
    print(s.id, s.s_name, s.age)
    return HttpResponse(f'查询成功--{s.id}--{s.s_name}--{s.age}')


def findAll(request):
    s_list = Student.objects.all()
    context = {
        's_list': s_list
    }
    # for s in s_list:
    #     context[s.id] = {'name': s.s_name, 'age': s.age}
    #     print(s.id, s.s_name, s.age)
    return render(request, 'stuList.html', context=context)


def delStu(request):
    s = Student.objects.get(pk=3)
    s.delete()
    return HttpResponse('删除成功')


def updateStu(request):
    s = Student.objects.get(pk=4)
    s.s_name = '大王'
    s.save()
    return HttpResponse('更新成功')


def addGrade(request):
    g = Grade()
    g.g_name = 'Python'
    g.save()
    g = Grade()
    g.g_name = 'HTML5'
    g.save()
    return HttpResponse('班级添加成功')


def gStus(request):
    g = Grade.objects.get(pk=1)
    s_list = g.student_set.all()
    for s in s_list:
        print(s.id, s.s_name, s.age)
    
    return HttpResponse('班级学生查询成功')


def stuGrade(request):
    s = Student.objects.get(pk=5)
    g_name = s.s_grade.g_name
    print(s.id, s.s_name, g_name)
    return HttpResponse(f'学生所属班级{g_name}')


def valuesStu(request):
    s = Student.objects.values()
    for i in s:
        print(i)
    return HttpResponse('values测试')


def findGrade(request):
    g_list = Grade.objects.all()
    context = {
        'g_list': g_list
    }
    return render(request, 'findGrade.html', context=context)


def graStu(request):
    g_name = request.GET.get('g_name')
    g = Grade.objects.filter(g_name=g_name)[0]
    s_list = Student.objects.filter(s_grade=g.id).all()
    context = {
        's_list': s_list
    }
    return render(request, 'graStu.html', context=context)
