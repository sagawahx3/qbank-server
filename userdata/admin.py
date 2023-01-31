from django.contrib import admin
from .models import UserData
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User


class UserDataInline(admin.StackedInline):
    model = UserData
    can_delete = False
    verbose_name_plural = 'userdata'


# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = [UserDataInline]


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)