# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-16 09:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20160916_1146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programstat',
            name='program_ended_datetime',
            field=models.DateTimeField(),
        ),
    ]