from django.db import models

class User(models.Model):
    fName = models.CharField (max_length=50, verbose_name = "First Name", blank = True)
    lName = models.CharField (max_length=50, verbose_name = "First Name", blank = True)

    def __unicode__(self):
        return u'%s, %s' % (self.lName, self.fName)
