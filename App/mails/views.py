# from django.shortcuts import render
from django.views.generic.edit import CreateView
# from .forms import ContactUsForm
from .models import ContactUs


class ContactUsView(CreateView):
    template_name = 'contactus_thanks.html'
    model = ContactUs
    fields = ['name', 'subject', 'message', 'email']
    success_url = "https://www.google.com"
