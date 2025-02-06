from django.contrib import admin

from .models import Quiz, Question, Choice, StudentAnswer


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ["id", "teacher", "name", "created_at"]


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 4

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ["id", "quiz"]
    inlines = [ChoiceInline]

@admin.register(StudentAnswer)
class StudentAnswerAdmin(admin.ModelAdmin):
    list_display = ["id", "student", "question", "selected_choice", "answered_at"]

