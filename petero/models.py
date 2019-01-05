# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Registration(models.Model):
    name = models.CharField(max_length=500)
    phone = models.CharField(max_length=100)
    idno = models.IntegerField()
    location = models.CharField(max_length=300)
    gender = models.CharField(max_length=300)
    maritus_status = models.CharField(max_length=100)
    dob = models.DateField()


class Jobs(models.Model):
    idno = models.IntegerField()
    department = models.CharField(max_length=300)
    position = models.CharField(max_length=300)
    salary = models.CharField(max_length=100)
    contract = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()


class Family(models.Model):
    idno = models.IntegerField()
    nxtname = models.CharField(max_length=300)
    phone = models.CharField(max_length=100)
    relationship = models.CharField(max_length=300)
    location = models.CharField(max_length=100)