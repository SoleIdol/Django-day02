# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2020-09-01 13:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0003_remove_student_s_grade'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='s_grade',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='App1.Grade'),
        ),
    ]
