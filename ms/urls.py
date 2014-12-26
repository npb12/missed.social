from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ms.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^user/', include('users.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^landing/$', TemplateView.as_view(template_name = "pages/ms/landing.html")),
)
