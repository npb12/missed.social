from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
#from tastypie.authentication import BasicAuthentication
from tastypie.authentication import ApiKeyAuthentication
from tastypie import fields
from users.models import Location, UserProfile

class UserResource(ModelResource):
  class Meta:
    queryset = UserProfile.objects.all()
    resource_name = 'user'
    authentication = ApiKeyAuthentication()
    authorization = Authorization()
    list_allowed_methods = ['get', 'patch', 'post']

class LocationResource(ModelResource):
  user = fields.ForeignKey(UserResource, 'user')

  class Meta:
    queryset = Location.objects.all()
    resource_name = 'location'
    filtering = {
      "user": ('exact'),
    }
    authentication = ApiKeyAuthentication()
    authorization = Authorization()
    list_allowed_methods = ['get', 'patch', 'post']
