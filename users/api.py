from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from tastypie.authentication import BasicAuthentication
from tastypie import fields
from users.models import Location, User

class UserResource(ModelResource):
  class Meta:
    queryset = User.objects.all()
    resource_name = 'user'

class LocationResource(ModelResource):
  user = fields.ForeignKey(UserResource, 'user')

  class Meta:
    queryset = Location.objects.all()
    resource_name = 'location'
