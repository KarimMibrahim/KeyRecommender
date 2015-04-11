from django.views.generic.base import TemplateView
from django.shortcuts import render
# from django.views.generic.list import ListView


class HomePage(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(HomePage, self).get_context_data(**kwargs)
        # context['Important keywords'] = Get the important keywords.
        return context


def search_view(request):
    if request.method == 'POST':
        print (request.POST['keywords'])

    return render(
        request,
        'search_results.html',
        {})
