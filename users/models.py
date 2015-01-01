from django.db import models
import datetime

class InterestType(models.Model):
  description = models.CharField (max_length=50, verbose_name = "Interest Type")

  def __unicode__(self):
    return self.description
  
class UserType(models.Model):
  description = models.CharField (max_length=50, verbose_name = "User Type")

  def __unicode__(self):
    return self.description

class User(models.Model):
  fName = models.CharField (max_length=50, verbose_name = "First Name", blank = True)
  lName = models.CharField (max_length=50, verbose_name = "First Name", blank = True)
  userType = models.ForeignKey(UserType, verbose_name = 'Related User Type', null = True)
  interestedIn = models.ForeignKey(InterestType, verbose_name = 'Related Interested Type', null = True)

  def __unicode__(self):
    return u'%s, %s' % (self.lName, self.fName)

class Location(models.Model):
  user = models.ForeignKey(User, verbose_name = 'Related User')
  latitude = models.DecimalField(max_digits = 10, decimal_places = 8, default = 1, verbose_name = 'Latitude')
  longitude = models.DecimalField(max_digits = 10, decimal_places = 8, default = 1, verbose_name = 'Longitude')
  timeStamp = models.DateTimeField(verbose_name = 'Time Stamp', default = datetime.datetime.now())

  def __unicode__(self):
    return u'%s - %s' % (self.user, self.timeStamp)

