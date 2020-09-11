from django.conf.urls import url

from App2 import views

urlpatterns = [
    url(r'^index/', views.index),
    url(r'^addDatetime/',views.addDatetime),
    url(r'^loadStatic/',views.loadStatic)
]
