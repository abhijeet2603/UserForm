from django.http import HttpResponse
from django.shortcuts import render


import re

from Form.models import FormInfo


# Create your views here.
def HomePage(request):
    return render(request, "index.html")

def form(request):
    if request.method == "POST":
        Name = request.POST.get('name')
        Dob = request.POST.get('dob')
        Email = request.POST.get('email')
        Mobile = request.POST.get('mobile')

        if not validate_mobile_number(Mobile):
            return HttpResponse("please enter a valid number")

        obj = FormInfo(Name=Name, Dob=Dob, Email=Email, Mobile=Mobile)
        obj.save()
        return HttpResponse("completed")


def validate_mobile_number(mobile_number):
    pattern = r'(0|91)?[5-9]\d{9}'
    return re.fullmatch(pattern, mobile_number) is not None

import re

from django.http import HttpResponse
from django.shortcuts import render, redirect

from Form.models import FormInfo
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.

def HomePage(request):
    return render(request, 'index.html')


def form(request):
    if request.method == "POST":
        Name = request.POST.get('name')
        Dob = request.POST.get('dob')
        Email = request.POST.get('email')
        Mobile = request.POST.get('mobile')

        if not validate_mobile_number(Mobile):
            return HttpResponse("Please enter a valid number")

        obj = FormInfo(Name=Name, Dob=Dob, Email=Email, Mobile=Mobile)
        obj.save()

        # Send email
        subject = 'Form Submission'
        message = f'Thank you for submitting the form, {Name}!'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [Email]
        send_mail(subject, message, email_from, recipient_list)

        # return HttpResponse("Form submitted successfully. Thank you!")
        return redirect('display_forms')


def validate_mobile_number(mobile_number):
    pattern = r'(0|91)?[5-9]\d{9}'
    return re.fullmatch(pattern, mobile_number) is not None


def display_forms(request):
    forms = FormInfo.objects.all()
    return render(request, 'display_forms.html', {'forms': forms})
