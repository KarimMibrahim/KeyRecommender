from django.views.generic.base import TemplateView
from django.shortcuts import render
# from django.views.generic.list import ListView


class HomePage(TemplateView):
    template_name = "index.html"


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
