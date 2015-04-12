from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.shortcuts import render
from mails.models import ContactUs


class HomePage(CreateView):
    template_name = "index.html"
    model = ContactUs
    fields = ['name', 'subject', 'message', 'email']
    success_url = "https://www.google.com"


def dataset_list_view(request):
    #returns all datasets we have.
    datasets = {}  # get datasets
    return render(
        request,
        'search_results.html',
        {"datasets": datasets})


def dataset_detail_view(request, dataset_id):
    # get the specific dataset by id
    dataset = dataset_id  # get the dataset using its id
    return render(
        request,
        'search_results.html',
        {"dataset": dataset})

# def search_view(request):
#     if request.method == 'POST':
#         keywords = request.POST['keywords']
#         print (request.POST['keywords'])

#     return render(
#         request,
#         'search_results.html',
#         {"keywords": keywords})
