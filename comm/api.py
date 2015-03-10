from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
#from tastypie.authentication import BasicAuthentication
from tastypie.authentication import ApiKeyAuthentication
from tastypie import fields
from users.models import Location
from comm.models import LocalPost, PostReply, MsgToUser, Wave
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django_facebook.models import FacebookCustomUser
User = get_user_model()

class LocalPostResource(ModelResource):
  class Meta:
    queryset = LocalPost.objects.all()
    resource_name = 'localPost'
    authentication = ApiKeyAuthentication()
    authorization = Authorization()
    list_allowed_methods = ['get', 'patch', 'post']

class PostReplyResource(ModelResource):
  class Meta:
    queryset = PostReply.objects.all()
    resource_name = 'postReply'
    authentication = ApiKeyAuthentication()
    authorization = Authorization()
    list_allowed_methods = ['get', 'patch', 'post']

class MsgToUserResource(ModelResource):
  class Meta:
    queryset = MsgToUser.objects.all()
    resource_name = 'msgToUser'
    authentication = ApiKeyAuthentication()
    authorization = Authorization()
    list_allowed_methods = ['get', 'patch', 'post']

class WaveResource(ModelResource):
  class Meta:
    queryset = Wave.objects.all()
    resource_name = 'wave'
    authentication = ApiKeyAuthentication()
    authorization = Authorization()
    list_allowed_methods = ['get', 'patch', 'post']


