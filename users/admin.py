from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ("username", "first_name", "last_name", "user_type","is_staff", "is_active")
    list_filter = ("user_type", )
    fieldsets = UserAdmin.fieldsets + (
        ("Additional info", {"fields": ("user_type", )}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional info", {"fields": ("user_type",) }),
    )


