from django.db import models
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django_facebook.utils import get_user_model, get_profile_model
from django_facebook.models import FacebookModel, FacebookCustomUser
from django.db.models.signals import post_save
from django.dispatch.dispatcher import receiver
User = get_user_model()
from ms import settings
import datetime


class Location(models.Model):
  user = models.ForeignKey(FacebookCustomUser, verbose_name = 'Related User')
  latitude = models.DecimalField(max_digits = 12, decimal_places = 8, default = 1, verbose_name = 'Latitude')
  longitude = models.DecimalField(max_digits = 12, decimal_places = 8, default = 1, verbose_name = 'Longitude')
  timeStamp = models.DateTimeField(verbose_name = 'Time Stamp', default = datetime.datetime.now())

  def __unicode__(self):
    return u'%s - %s [Lng: %s | Lat: %s]' % (self.user, self.timeStamp, self.longitude, self.latitude)


class Encounter(models.Model):
  user = models.ForeignKey(FacebookCustomUser, verbose_name = 'Related User', related_name = "user")
  encounter = models.OneToOneField(User, verbose_name = 'Encounted User', related_name = "encounter")
  userLoc = models.ForeignKey(Location, verbose_name = 'User\'s Location', related_name = "userLoc")
  encounterLoc = models.ForeignKey(Location, verbose_name = 'Encounted User\'s Location', related_name = "encounterLoc")

  def __unicode__(self):
    return u'%s (%s) - %s (%s)' % (self.user, self.userLoc , self.encounter, self.encounterLoc)

