from django.conf.urls import url

from App1 import views

urlpatterns=[
    url(r'^index/',views.index),
    url(r'^foods/',views.foods),
    url(r'^addStudent/',views.addStudent),
    url(r'^selectStudent/',views.selectStudent),
    url(r'^findAll/',views.findAll),
    url(r'^delStu',views.delStu),
    url(r'^updateStu',views.updateStu),
    url(r'^addGrade/',views.addGrade),
    url(r'^gStus/',views.gStus),
    url(r'^stuGrade/',views.stuGrade),
    url(r'^valuesStu/',views.valuesStu),
    url(r'^findGrade/',views.findGrade),
    url(r'^graStu/',views.graStu)
]