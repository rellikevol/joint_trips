from django.contrib import admin
from users.models import Profile, Chat, Message

# Register your models here.
admin.site.register(Profile)
admin.site.register(Chat)
admin.site.register(Message)