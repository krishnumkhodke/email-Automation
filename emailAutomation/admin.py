from django.contrib import admin
from . models import SendNewEmail, SentEmail

# Register your models here.

admin.site.register(SendNewEmail)
admin.site.register(SentEmail)