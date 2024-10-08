from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
# Register your models here.
class UserProfileInline(admin.StackedInline):
    model = CustomUser

class UserAdmin(UserAdmin):
    inlines = (UserProfileInline,)
    
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
