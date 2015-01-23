from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)
import datetime

class InterestType(models.Model):
  description = models.CharField (max_length=50, verbose_name = "Interest Type")

  def __unicode__(self):
    return self.description
  
class UserType(models.Model):
  description = models.CharField (max_length=50, verbose_name = "User Type")

  def __unicode__(self):
    return self.description

class UserManager(BaseUserManager):
  def create_user(self, email, password=None):
    if not email: 
      raise ValueError('You need a valid email address to register')

    user = self.model(
      email = self.normalize_email(email),
    )
    

    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_superuser(self, email, password=None):
    user = self.create_user(email, password=password)
    user.is_admin = True
    user.save(using=self._db)
    return user

class UserProfile(AbstractBaseUser):
  email = models.EmailField(max_length=255, verbose_name = "Email Address", unique = True)
  fName = models.CharField (max_length=50, verbose_name = "First Name", blank = True)
  userType = models.ForeignKey(UserType, verbose_name = 'Related User Type', null = True)
  interestedIn = models.ForeignKey(InterestType, verbose_name = 'Related Interested Type', null = True)
  is_active = models.BooleanField(default=True)
  is_admin = models.BooleanField(default=False)

  objects = UserManager()

  USERNAME_FIELD = 'email'

  def get_full_name(self):
    # The user is identified by their email address
    return self.email

  def get_short_name(self):
     # The user is identified by their email address
    return self.email

  def __str__(self):              # __unicode__ on Python 2
    return self.email

  def has_perm(self, perm, obj=None):
    "Does the user have a specific permission?"
    # Simplest possible answer: Yes, always
    return True

  def has_module_perms(self, app_label):
    "Does the user have permissions to view the app `app_label`?"
    # Simplest possible answer: Yes, always
    return True


  @property
  def is_staff(self):
    return self.is_admin

class Location(models.Model):
  user = models.ForeignKey(UserProfile, verbose_name = 'Related User')
  latitude = models.DecimalField(max_digits = 12, decimal_places = 8, default = 1, verbose_name = 'Latitude')
  longitude = models.DecimalField(max_digits = 12, decimal_places = 8, default = 1, verbose_name = 'Longitude')
  timeStamp = models.DateTimeField(verbose_name = 'Time Stamp', default = datetime.datetime.now())

  def __unicode__(self):
    return u'%s - %s [Lng: %s | Lat: %s]' % (self.user, self.timeStamp, self.longitude, self.latitude)


class Encounter(models.Model):
  user = models.ForeignKey(UserProfile, verbose_name = 'Related User', related_name = "user")
  encounter = models.ForeignKey(UserProfile, verbose_name = 'Encounted User', related_name = "encounter")
  userLoc = models.ForeignKey(Location, verbose_name = 'User\'s Location', related_name = "userLoc")
  encounterLoc = models.ForeignKey(Location, verbose_name = 'Encounted User\'s Location', related_name = "encounterLoc")

  def __unicode__(self):
    return u'%s (%s) - %s (%s)' % (self.user, self.userLoc , self.encounter, self.encounterLoc)
