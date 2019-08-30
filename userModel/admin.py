from django.contrib import admin

# Register your models here.


# Register your models here.
from .models import UserModel


# Register your models here.
class UserModelAdmin(admin.ModelAdmin):
    list_display = ['user']


admin.site.register(UserModel, UserModelAdmin)
