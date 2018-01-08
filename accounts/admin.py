from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as UserAdminBase
from django.contrib.auth.models import Group
from accounts.models import User

admin.site.unregister(Group)

class UserAdmin(UserAdminBase):
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    ordering = ('email',)
admin.site.register(User, UserAdmin)
