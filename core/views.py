from django.shortcuts import render,redirect
from .models import Contact
from django.contrib import messages

import os
from django.conf import settings
from django.http import HttpResponse, Http404

from .utils import send_mail_to_me


# Create your views here.
def contact_form(request, *args, **kwargs):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact = Contact()
        contact.name = name
        contact.email = email
        contact.messages = message
        contact.save()
        messages.success(request,"Thanks for Your Message! Contact You Shortly.")
        send_mail_to_me(name,'ronniloreo@gmail.com',message,email,phone = 'No Phone',extra_field=' ')
        return redirect('/')
    return render(request, 'index.html')


def awareness_program_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        phone = request.POST.get('phone')
        contact = Contact()
        contact.name = name
        contact.email = email
        contact.messages = message
        contact.phone = phone
        contact.is_through_atc = True
        contact.save()
        messages.success(request,"Thanks for Your Message! We'll Contact You Shortly.")
        send_mail_to_me(name,'ronniloreo@gmail.com',message,email,phone,extra_field="From ATC")
        return redirect('core:awareness-through-code-program')
    return render(request, 'awareness_through_code.html')


def getpdf(request):  
    file_path = 'templates/resume/ravi.pdf'
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    else:
        raise Http404