# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-05-25 13:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petero', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='location',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='registration',
            name='maritus_status',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='registration',
            name='phone',
            field=models.CharField(max_length=100),
        ),
    ]
