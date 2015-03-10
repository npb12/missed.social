from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
admin.autodiscover()
from users.api import UserResource, LocationResource
from comm.api import LocalPostResource, PostReplyResource, MsgToUserResource, WaveResource
from users.views import *

from tastypie.api import Api


v1_api = Api(api_name='v1')
v1_api.register(UserResource())
v1_api.register(LocationResource())
v1_api.register(LocalPostResource())
v1_api.register(PostReplyResource())
v1_api.register(MsgToUserResource())
v1_api.register(WaveResource())

user_resource = UserResource()

urlpatterns = patterns('',
    url(r'^profile/(?P<userPK>\d*)/$', profile),
    url(r'^all/$', all_users),
    url(r'^all/$', all_users),
    url(r'^home/$', home),
    url(r'^user-details/$', user_details),
    url(r'^plot-gps-points/(?P<userPK>\d*)/$', plot_gps_points),
    url(r'^gmap-user-data/$', gmap_user_data),
    url(r'^delete-all-data-points/$', delete_all_data_points),
    url(r'^get-encounters/$', get_encounters),
    url(r'^sort-data/$', sort_data_points),
    url(r'^api/', include(v1_api.urls)),
    url(r'^app-registration/', app_registration),
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
