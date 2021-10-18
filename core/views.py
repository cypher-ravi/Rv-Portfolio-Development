from django.shortcuts import render,redirect
from .models import Contact
from django.contrib import messages

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
        return redirect('/')
    return render(request, 'index.html')


def awareness_program_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact = Contact()
        contact.name = name
        contact.email = email
        contact.messages = message
        contact.is_through_atc = True
        contact.save()
        messages.success(request,"Thanks for Your Message! We'll Contact You Shortly.")
        return redirect('core:awareness-through-code-program')
    return render(request, 'awareness_through_code.html')