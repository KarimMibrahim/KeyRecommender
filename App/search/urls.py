from django.conf.urls import url
from .views import list_keywords


urlpatterns = [
    url(r'^$', list_keywords, name='list_datasets'),
    # url(r'^(?P<dataset_id>\d+)/$', dataset_detail_view, name='detail_datasets'),
]
