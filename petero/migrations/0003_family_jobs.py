# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-12-20 12:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petero', '0002_auto_20180525_1624'),
    ]

    operations = [
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idno', models.IntegerField()),
                ('nxtname', models.CharField(max_length=300)),
                ('phone', models.CharField(max_length=100)),
                ('relationship', models.CharField(max_length=300)),
                ('location', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idno', models.IntegerField()),
                ('department', models.CharField(max_length=300)),
                ('position', models.CharField(max_length=300)),
                ('salary', models.IntegerField()),
                ('contract', models.CharField(max_length=100)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
        ),
    ]
