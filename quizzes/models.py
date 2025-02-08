from django.db import models

from groups.models import Group
from users.models import User


class Quiz(models.Model):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='quizzes')
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    groups = models.ManyToManyField(Group, related_name="quizzes")

    objects = models.Manager()

    def __str__(self):
        return f"Author: {self.teacher}, Quiz name: {self.name}"

    class Meta:
        verbose_name = "Quiz"
        verbose_name_plural = "Quizzes"


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    text = models.TextField()

    objects = models.Manager()

    def __str__(self):
        return f"{self.quiz.name} - {self.text[:50]}"

    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Questions"


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    text = models.CharField(max_length=150)
    is_correct = models.BooleanField(default=False)

    objects = models.Manager()

    def __str__(self):
        return f"{self.question.text[:20]} - {self.text}"

    class Meta:
        verbose_name = "Choice"
        verbose_name_plural = "Choices"
