# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-12-21 08:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petero', '0003_family_jobs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='salary',
            field=models.CharField(max_length=100),
        ),
    ]
