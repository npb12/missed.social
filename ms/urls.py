from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.contrib import admin

from ms.views import sample_gps_data
from users.views import register

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ms.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^accounts/$', include('django_facebook.auth_urls')),
    url(r'^user/', include('users.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^join/', register),
    url(r'^main/$', TemplateView.as_view(template_name = "basics/base.html")),
    url(r'^sample-data/$', sample_gps_data, name='create_sample_gps_data'),
    url(r'^$', TemplateView.as_view(template_name = "basics/landing.html")),
    url(r'^facebook/', include('django_facebook.urls')),
    url(r'^accounts/', include('django_facebook.auth_urls')),
)
