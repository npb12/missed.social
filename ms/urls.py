from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.contrib import admin

from ms.views import sample_gps_data

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ms.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^user/', include('users.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^landing/$', TemplateView.as_view(template_name = "pages/ms/landing.html")),
    url(r'^sample-data/$', sample_gps_data, name='create_sample_gps_data'),
    url(r'^$', TemplateView.as_view(template_name = "pages/ms/landing.html")),
)
