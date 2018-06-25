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