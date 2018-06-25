# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response


# Create your views here.
from django.template.response import TemplateResponse

from petero.models import Registration


def mylogin(request):
    return render_to_response('index.html')


def dashboard(request):
    return render_to_response('dashboard.html')


def registration(request):
    dat = Registration.objects.all()
    return TemplateResponse(request, 'registration.html', {"data": dat})

def job(request):
    return render_to_response('job.html')


def family(request):
    return render_to_response('family.html')


def saveReg(request):
    name = request.POST["name"]
    phone = request.POST["phone"]
    idno = request.POST["idno"]
    location = request.POST["location"]
    gender = request.POST["gender"]
    maritus_status = request.POST["status"]
    dob = request.POST["dob"]
    reg_detail = Registration(name=name, phone=phone, idno=idno, location=location, gender=gender, maritus_status = maritus_status, dob=dob)
    reg_detail.save()
    print ("Registration Saved")
    dat = Registration.objects.all()
    return render(request, "registration.html", {"data": dat})

