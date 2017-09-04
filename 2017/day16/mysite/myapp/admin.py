from django.contrib import admin
from myapp import models
# Register your models here.

admin.site.register(models.UserInfo)
admin.site.register(models.UserType)