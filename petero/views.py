# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response


# Create your views here.
from django.template.response import TemplateResponse

from petero.models import *
import logging
logging=logging.getLogger('registration')


def mylogin(request):
    return render_to_response('index.html')


def dashboard(request):
    return render_to_response('dashboard.html')


def registration(request):
    logging.info("---loading Registrations--")
    dat = Registration.objects.all()
    return TemplateResponse(request, 'registration.html', {"data": dat})


def job(request):
    logging.info("---loading Jobs--")
    dat = Jobs.objects.all()
    return TemplateResponse(request, 'job.html', {"data": dat})


def family(request):
    logging.info("---loading Family--")
    dat = Family.objects.all()
    print(dat[0].phone)
    return TemplateResponse(request, 'family.html', {"data": dat})


def saveReg(request):
    name = request.POST["name"]
    phone = request.POST["phone"]
    idno = request.POST["idno"]
    location = request.POST["location"]
    gender = request.POST["gender"]
    maritus_status = request.POST["status"]
    dob = request.POST["dob"]
    reg_detail = Registration(name=name, phone=phone, idno=idno, location=location, gender=gender, maritus_status = maritus_status, dob=dob)
    logging.info("---Saving registrations--")
    reg_detail.save()
    logging.info("---Registration Saved--")
    dat = Registration.objects.all()
    return render(request, "registration.html", {"data": dat})


def saveFamily(request):
    idno = request.POST["idno"]
    nxtname = request.POST["nxtname"]
    phone = request.POST["phone"]
    relationship = request.POST["relationship"]
    location = request.POST["location"]
    family_detail = Family(idno=idno, nxtname=nxtname, phone=phone, relationship=relationship, location=location)
    logging.info("---Saving Family--")
    family_detail.save()
    logging.info("---Family Saved--")
    dat = Family.objects.all()
    return render(request, "family.html", {"data": dat})


def saveJob(request):
    idno = request.POST["id-no"]
    department = request.POST["department"]
    position = request.POST["position"]
    salary = request.POST["salary"]
    contract = request.POST["contract"]
    start_date = request.POST["start-date"]
    end_date = request.POST["end-date"]
    print(idno)
    print(department)
    print(position)
    print(salary)
    job_detail = Jobs(idno=idno, department=department, position=position, salary=salary, contract=contract, start_date=start_date, end_date=end_date)
    logging.info("---Saving Job--")
    job_detail.save()
    logging.info("---Job Saved--")
    dat = Jobs.objects.all()
    return render(request, "job.html", {"data": dat})


def DeleteFamily(request):
    if request.method == 'POST':
        id_no = request.POST['idno']
    family = Family.objects.get(idno=id_no)
    family.delete()
    dat = Family.objects.all()
    return render(request, "family.html", {"data": dat})




