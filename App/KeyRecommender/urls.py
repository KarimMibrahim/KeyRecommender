from django.conf.urls import include, url
from django.contrib import admin
from search.views import HomePage


urlpatterns = [
    # Examples:
    url(r'^$', HomePage.as_view(), name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^search/', include('search.urls', namespace='search')),

    url(r'^admin/', include(admin.site.urls)),
]
