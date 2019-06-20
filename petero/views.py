# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response


# Create your views here.
from django.template.response import TemplateResponse
from django.contrib import messages

from petero.models import *
import logging
logging=logging.getLogger('registration')


def mylogin(request):
    return render_to_response('index.html')


def dashboard(request):
    data = []
    reg = Registration.objects.count()
    fam = Family.objects.count()
    job = Jobs.objects.count()
    data.append(reg)
    data.append(fam)
    data.append(job)
    print(data)
    return render_to_response('dashboard.html', {"data": data})


def registration(request):
    logging.info("---loading Registrations--")
    dat = Registration.objects.all()
    return TemplateResponse(request, 'registration.html', {"data": dat})


def job(request):
    logging.info("---loading Jobs--")
    dat = Registration.objects.all()
    return TemplateResponse(request, 'job.html', {"reg": dat})


def family(request):
    logging.info("---loading Family--")
    dat = Registration.objects.all()
    # print(dat[0].phone)
    return TemplateResponse(request, 'family.html', {"reg": dat})


def saveReg(request):
    name = request.POST["name"]
    phone = request.POST["phone"]
    idno = request.POST["idno"]
    location = request.POST["location"]
    gender = request.POST["gender"]
    maritus_status = request.POST["status"]
    dob = request.POST["dob"]
    try:
        reg_detail = Registration(name=name, phone=phone, idno=idno, location=location, gender=gender,
                                  maritus_status=maritus_status, dob=dob)
        logging.info("---Saving registrations--")
        reg_detail.save()
        logging.info("---Registration Saved--")
        messages.info(request, "Registration Saved Successfully!")
    except IndexError:
        logging.info("Registration Not Saved")
        messages.error(request, "Registration Not Saved")

    dat = Registration.objects.all()
    return render(request, "registration.html", {"data": dat})


def editReg(request):
    name = request.POST["edit_name"]
    phone = request.POST["edit_phone"]
    idno = request.POST["edit_idno"]
    location = request.POST["edit_location"]
    maritus_status = request.POST["edit_status"]
    try:
        reg_detail = Registration.objects.filter(idno=idno)
        logging.info("---Updating registrations--")
        reg_detail.update(name=name, phone=phone, location=location, maritus_status=maritus_status)
        logging.info("---Registration Saved--")
        messages.info(request, 'Updated successfully!')
    except IndexError:
        messages.error(request, 'Error in Updating !')
        logging.info("---Registration Not Updated--")

    dat = Registration.objects.all()
    return render(request, "registration.html", {"data": dat})


def deleteReg(request):
    name = request.POST["delete_name"]
    phone = request.POST["delete_phone"]
    idno = request.POST["delete_idno"]
    try:
        reg_detail = Registration.objects.filter(name=name, phone=phone, idno=idno)
        logging.info("---Deleting registrations--")
        reg_detail.delete()
        logging.info("---Registration Deleted--")
        job_detail = Jobs.objects.filter(idno=idno)
        logging.info("---Deleting Job--")
        job_detail.delete()
        logging.info("---Job Detail Deleted--")
        family_detail = Family.objects.filter(idno=idno)
        logging.info("---Deleting Family Detail--")
        family_detail.delete()
        logging.info("---Family Detail Deleted--")
        messages.info(request, "Registration Deleted Successfully!")
    except IndexError:
        messages.error(request, "Error in Deleting Registration")

    dat = Registration.objects.all()
    return render(request, "registration.html", {"data": dat})


def saveFamily(request):
    idno = request.POST["idno"]
    nxtname = request.POST["nxtname"]
    phone = request.POST["phone"]
    relationship = request.POST["relationship"]
    location = request.POST["location"]
    try:
        family_detail = Family(idno=idno, nxtname=nxtname, phone=phone, relationship=relationship, location=location)
        logging.info("---Saving Family--")
        family_detail.save()
        logging.info("---Family Saved--")
        messages.info(request, "Family Detail Saved")
    except IndexError:
        logging.info("Error in Saving Family")
        messages.error(request, "Error in Saving Family Details")

    dat = Registration.objects.all()
    return render(request, "family.html", {"reg": dat})


def viewFamily(request):
    logging.info("--Loading Families---")
    dat = Family.objects.all()
    return render(request, "family.html", {"data": dat})


def editFamily(request):
    idno = request.POST["edit_idno"]
    nxtname = request.POST["edit_nxtname"]
    phone = request.POST["edit_phone"]
    relationship = request.POST["edit_relationship"]
    location = request.POST["edit_location"]
    try:
        family_detail = Family.objects.filter(idno=idno)
        logging.info("---Editing Family--")
        family_detail.update(nxtname=nxtname, phone=phone, relationship=relationship, location=location)
        logging.info("---Family Edited--")
        messages.info(request, "Family Edited Successfully!")
    except IndexError:
        logging.info("Error in Editing Family")
        messages.error(request, "Error in Editing Family")

    dat = Registration.objects.all()
    return render(request, "family.html", {"reg": dat})


def saveJob(request):
    idno = request.POST["idno"]
    department = request.POST["department"]
    position = request.POST["position"]
    salary = request.POST["salary"]
    contract = request.POST["contract"]
    start_date = request.POST["start_date"]
    end_date = request.POST["end_date"]
    try:
        job_detail = Jobs(idno=idno, department=department, position=position, salary=salary, contract=contract,
                          start_date=start_date, end_date=end_date)
        logging.info("---Saving Job--")
        job_detail.save()
        logging.info("---Job Saved--")
        messages.info(request, "Job Saved Successfully!")
    except IndexError:
        logging.info("Error in Saving Job")
        messages.error(request, "Error in Saving Job")

    dat = Registration.objects.all()
    return render(request, "job.html", {"reg": dat})


def viewJob(request):
    logging.info("--Loading Jobs---")
    dat = Jobs.objects.all()
    return render(request, "job.html", {"data": dat})


def editJob(request):
    idno = request.POST["edit_idno"]
    department = request.POST["edit_department"]
    position = request.POST["edit_position"]
    salary = request.POST["edit_salary"]
    contract = request.POST["edit_contract"]
    end_date = request.POST["edit_end_date"]
    try:
        job_detail = Jobs.objects.filter(idno=idno)
        logging.info("---Editing Job--")
        job_detail.update(department=department, position=position, salary=salary, contract=contract,
                          end_date=end_date)
        logging.info("---Job Edited--")
        messages.info(request, "Job Edited Details Successfully!")
    except IndexError:
        logging.info("Error in Editing Job")
        messages.error(request, "Error in Editing Job Details")

    dat = Registration.objects.all()
    return render(request, "job.html", {"reg": dat})







