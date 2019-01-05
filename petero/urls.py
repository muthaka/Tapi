from django.conf.urls import url
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth

from . import views

urlpatterns = [
    url(r'^$', views.mylogin, name='login'),
    url(r'^dashboard', views.dashboard, name='dashboard'),
    url(r'^Registration', views.registration, name='reg'),
    url(r'^Job', views.job, name='job'),
    url(r'^Family', views.family, name='family'),
    url(r'^saveRegistration', views.saveReg, name='saveReg'),
    url(r'^saveJob', views.saveJob, name='saveJob'),
    url(r'^saveFamily', views.saveFamily, name='saveFamily'),
    url(r'^deleteFamily', views.DeleteFamily, name='deleteFamily'),
]
