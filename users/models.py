from django.db import models
import datetime

class User(models.Model):
  fName = models.CharField (max_length=50, verbose_name = "First Name", blank = True)
  lName = models.CharField (max_length=50, verbose_name = "First Name", blank = True)

  def __unicode__(self):
    return u'%s, %s' % (self.lName, self.fName)

class Location(models.Model):
  user = models.ForeignKey(User, verbose_name = 'Related User')
  latitude = models.DecimalField(max_digits = 10, decimal_places = 5, default = 1, verbose_name = 'Latitude')
  longitude = models.DecimalField(max_digits = 10, decimal_places = 5, default = 1, verbose_name = 'Longitude')
  timeStamp = models.DateField(verbose_name = 'Time Stamp', default = datetime.datetime.now())

  def __unicode__(self):
    return u'%s - %s' % (self.user, self.timeStamp)
