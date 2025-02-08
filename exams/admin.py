from django.contrib import admin
from .models import TestSession, StudentAnswer, TestResult


admin.site.register(TestSession)
admin.site.register(StudentAnswer)
admin.site.register(TestResult)
