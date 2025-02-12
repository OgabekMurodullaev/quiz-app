from django.contrib import admin
from .models import TestSession, StudentAnswer, TestResult


class TestSessionAdmin(admin.ModelAdmin):
    list_display = ["id", "student"]


class StudentAnswerAdmin(admin.ModelAdmin):
    list_display = ["id", "session", "question"]


class TestResultAdmin(admin.ModelAdmin):
    list_display = ["id", "session"]

admin.site.register(TestSession, TestSessionAdmin)
admin.site.register(StudentAnswer, StudentAnswerAdmin)
admin.site.register(TestResult, TestResultAdmin)
