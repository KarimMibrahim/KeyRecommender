from django.conf.urls import url
from .views import dataset_list_view, dataset_detail_view


urlpatterns = [
    url(r'^$', dataset_list_view, name='list_datasets'),
    url(r'^(?P<dataset_id>\d+)/$', dataset_detail_view, name='detail_datasets'),
]
