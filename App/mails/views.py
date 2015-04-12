from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import ContactUsForm


class ContactUsView(FormView):
    template_name = 'contactus_thanks.html'
    form_class = ContactUsForm
