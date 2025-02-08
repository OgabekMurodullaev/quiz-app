from django.contrib import admin

from .models import Quiz, Question, Choice


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ["id", "teacher", "name", "created_at"]


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 0

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ["id", "quiz"]
    inlines = [ChoiceInline]


