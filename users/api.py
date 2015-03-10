from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
#from tastypie.authentication import BasicAuthentication
from tastypie.authentication import ApiKeyAuthentication
from tastypie import fields
from users.models import Location
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django_facebook.models import FacebookCustomUser
User = get_user_model()

class UserResource(ModelResource):
  class Meta:
    #queryset = UserProfile.objects.all()
    #queryset = User.objects.all()
    queryset = FacebookCustomUser.objects.all()
    resource_name = 'user'
    authentication = ApiKeyAuthentication()
    authorization = Authorization()
    list_allowed_methods = ['get', 'patch', 'post']

class LocationResource(ModelResource):
  user = fields.ForeignKey(UserResource, 'user')

  """
  def obj_create(self, bundle, **kwargs):
    bundle = super(LocationResource, self).obj_create(bundle, **kwargs)
    print("hello!!")
    return bundle
  """

  class Meta:
    queryset = Location.objects.all()
    resource_name = 'location'
    """
    filtering = {
      "user": ('exact'),
    }
    """
    authentication = ApiKeyAuthentication()
    authorization = Authorization()
    list_allowed_methods = ['get', 'patch', 'post']
