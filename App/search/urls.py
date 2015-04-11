from django.conf.urls import url
from .views import search_view


urlpatterns = [
    url(r'^$', search_view, name='Search'),
]
