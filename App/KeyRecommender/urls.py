from django.conf.urls import include, url
from django.contrib import admin
from search.views import HomePage
from mails.views import ContactUsView


urlpatterns = [
    # Examples:
    url(r'^$', HomePage.as_view(), name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^datasets/', include('search.urls', namespace='search')),
    url(r'^contactus/', ContactUsView.as_view(), name='contactus'),

    url(r'^admin/', include(admin.site.urls)),
]
