from django.contrib import admin

from groups.models import Group
from users.models import User


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "teacher")
    filter_horizontal = ('student',)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "teacher":
            kwargs["queryset"] = User.objects.filter(user_type="teacher")
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "student":
            kwargs["queryset"] = User.objects.filter(user_type="student")
        return super().formfield_for_manytomany(db_field, request, **kwargs)
