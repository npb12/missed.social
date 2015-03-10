from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from models import Location, Encounter

admin.site.register(Location)
admin.site.register(Encounter)

# Register your models here.
