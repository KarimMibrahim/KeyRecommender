from django.conf.urls import url
from .views import list_keywords, dataset_detail_view


urlpatterns = [
    url(r'^$', list_keywords, name='list_datasets'),
    url(r'^(?P<dataset_name>\w+)/$', dataset_detail_view, name='detail_datasets'),
]
