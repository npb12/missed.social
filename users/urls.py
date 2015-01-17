from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from tastypie.api import Api
admin.autodiscover()

from users.api import UserResource, LocationResource
from users.views import *

v1_api = Api(api_name='v1')
v1_api.register(UserResource())
v1_api.register(LocationResource())

user_resource = UserResource()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'scrum.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^profile/$', TemplateView.as_view(template_name = "pages/users/profile.html")),
    url(r'^all/$', all_users),
    url(r'^user-details/(?P<userPK>\d*)/$', user_details),
    url(r'^plot-gps-points/(?P<userPK>\d*)/$', plot_gps_points),
    url(r'^gmap-user-data/$', gmap_user_data),
    url(r'^delete-all-data-points/$', delete_all_data_points),
    url(r'^get-encounters/(?P<userPK>\d*)/(?P<timeFrame>\d*)/$', find_encounters),
    url(r'^api/', include(v1_api.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.STATIC_ROOT,
        }),
)
