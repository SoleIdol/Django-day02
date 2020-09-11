from django.db import models


# Create your models here.

class Grade(models.Model):
    g_name = models.CharField(max_length=32)
    
    class Meta:
        db_table = 'grade'


class Student(models.Model):
    s_name = models.CharField(max_length=32, default='jack')
    age = models.IntegerField(default=22)
    s_grade = models.ForeignKey(Grade, default='1')
    
    class Meta:
        db_table = 'student'
