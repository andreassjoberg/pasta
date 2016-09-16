# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-16 09:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='programstat',
            old_name='program_executed_datetime',
            new_name='program_started_datetime',
        ),
        migrations.AddField(
            model_name='programstat',
            name='program_ended_datetime',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]
