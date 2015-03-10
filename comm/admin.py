from django.contrib import admin

from models import LocalPost, PostReply, MsgToUser, Wave

admin.site.register(LocalPost)
admin.site.register(PostReply)
admin.site.register(MsgToUser)
admin.site.register(Wave)


# Register your models here.
