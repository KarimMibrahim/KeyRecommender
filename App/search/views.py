from django.views.generic.edit import CreateView
from django.shortcuts import render
from mails.models import ContactUs


class HomePage(CreateView):
    template_name = "index.html"
    model = ContactUs
    fields = ['name', 'subject', 'message', 'email']
    success_url = "https://www.google.com"


def list_keywords(request):
    keywords = ['ahmed', 'sa3d', 'hi']  # get the dataset using its id
    return render(
        request,
        'search_results.html',
        {"keywords": keywords})


def dataset_detail_view(request, dataset_name):
    # get the specific dataset by id
    keywords = dataset_name  # get the dataset using its id
    return render(
        request,
        'search_results.html',
        {"keywords": keywords,
        "dataset_name": dataset_name})

# def search_view(request):
#     if request.method == 'POST':
#         keywords = request.POST['keywords']
#         print (request.POST['keywords'])

#     return render(
#         request,
#         'search_results.html',
#         {"keywords": keywords})
