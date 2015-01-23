from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from models import UserProfile, Location, InterestType, UserType

admin.site.register(UserProfile)
admin.site.register(Location)
admin.site.register(InterestType)
admin.site.register(UserType)

# Register your models here.
