from django.db import models
from django.forms import ModelForm
from django_facebook.utils import get_user_model, get_profile_model
from django_facebook.models import FacebookModel, FacebookCustomUser
import datetime


class LocalPost(models.Model):
  user = models.ForeignKey(FacebookCustomUser, verbose_name = 'Related User')
  latitude = models.DecimalField(max_digits = 12, decimal_places = 8, default = 1, verbose_name = 'Latitude')
  longitude = models.DecimalField(max_digits = 12, decimal_places = 8, default = 1, verbose_name = 'Longitude')
  timeStamp = models.DateTimeField(verbose_name = 'Time Stamp', default = datetime.datetime.now())
  msg = models.TextField(verbose_name = "Message", blank = True, null = True)

  def __unicode__(self):
    return u'%s [%s]' % (self.user, self.timeStamp)

class PostReply(models.Model):
  post = models.ForeignKey(LocalPost, verbose_name = "Related Post")
  user = models.ForeignKey(FacebookCustomUser, related_name = "PostReply_user", verbose_name = 'Related User')
  timeStamp = models.DateTimeField(verbose_name = 'Time Stamp', default = datetime.datetime.now())
  msg = models.TextField(verbose_name = "Reply", blank = True, null = True)
  
  def __unicode__(self):
    return u'Reply: %s [%s]' % (self.user, self.post)

class MsgToUser(models.Model):
  fromUser = models.ForeignKey(FacebookCustomUser, related_name = "msg_fromUser", verbose_name = 'Related User')
  toUser = models.ForeignKey(FacebookCustomUser, related_name = "msg_toUser", verbose_name = 'Related User')
  timeStamp = models.DateTimeField(verbose_name = 'Time Stamp', default = datetime.datetime.now())
  msg = models.TextField(verbose_name = "Message", blank = True, null = True)
  isRead = models.BooleanField(verbose_name = "Message Read", default = False)

  def __unicode__(self):
    return u'%s [%s]' % (self.user, self.timeStamp)


class Wave(models.Model):
  ACCEPTED_OPTIONS = (
    ('U', 'Undecided'),
    ('A', 'Accepted'),
    ('D', 'Declined'),
  )
  fromUser = models.ForeignKey(FacebookCustomUser, related_name = "wave_fromUser", verbose_name = 'Related User')
  toUser = models.ForeignKey(FacebookCustomUser, related_name = "wave_toUser", verbose_name = 'Related User')
  timeStamp = models.DateTimeField(verbose_name = 'Time Stamp', default = datetime.datetime.now())
  isAccepted = models.CharField(max_length = 2, verbose_name = "Wave Accepted", default = 'U', choices = ACCEPTED_OPTIONS)
  isSeen = models.BooleanField(verbose_name = "Wave Seen", default = False)
  

