from django.db import models


# Create your models here.

class Dog(models.Model):
    d_name = models.CharField(max_length=32)
    d_age = models.IntegerField()
    
    class Meta:
        db_table = 'dog'


class DatetimeTest(models.Model):
    d_time = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'datetimeTest'
