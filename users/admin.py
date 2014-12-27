from django.contrib import admin
from models import User, Location, InterestType, UserType

admin.site.register(User)
admin.site.register(Location)
admin.site.register(InterestType)
admin.site.register(UserType)

# Register your models here.
