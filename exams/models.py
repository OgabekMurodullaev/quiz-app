from datetime import timedelta

from django.db import models
from django.utils.timezone import now

from quizzes.models import Quiz, Question, Choice
from users.models import User



class TestSession(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name="test_sessions")
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name="test_sessions")
    started_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)  # Tugash vaqtini saqlash
    score = models.FloatField(default=0.0)
    is_completed = models.BooleanField(default=False)

    objects = models.Manager()

    def __str__(self):
        return f"{self.student.username} - {self.quiz.name} - {self.score}"

    def save(self, *args, **kwargs):
        if not self.started_at:
            self.started_at = now()

        if not self.completed_at:
            self.completed_at = self.started_at + timedelta(minutes=self.quiz.duration)  # ✅ Quiz modelidan duration olinadi

        super().save(*args, **kwargs)

        if self.is_completed:
            correct_answers = self.result.correct_answers if hasattr(self, 'result') else 0
            self.score = correct_answers * 5
            super().save(update_fields=['score'])



class StudentAnswer(models.Model):
    session = models.ForeignKey(TestSession, on_delete=models.CASCADE, related_name="answers")
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="student_answers")
    selected_choice = models.ForeignKey(Choice, on_delete=models.SET_NULL, related_name="student_answers", null=True, blank=True)
    is_correct = models.BooleanField(default=False)
    answered_at = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    def save(self, *args, **kwargs):
        if self.selected_choice and self.selected_choice.is_correct:
            self.is_correct = True
        else:
            self.is_correct = False

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.session.student.username} - {self.question.text[:20]} - {self.is_correct}"


class TestResult(models.Model):
    session = models.OneToOneField(TestSession, on_delete=models.CASCADE, related_name="result")
    correct_answers = models.PositiveIntegerField(default=0)
    incorrect_answers = models.PositiveIntegerField(default=0)
    total_score = models.FloatField(default=0.0)

    objects = models.Manager()

    def save(self, *args, **kwargs):
        self.correct_answers = self.session.answers.filter(is_correct=True).count()
        self.incorrect_answers = self.session.answers.filter(is_correct=False).count()
        self.total_score = (self.correct_answers / self.session.quiz.questions.count()) * 100

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.session.student.username} - {self.total_score} %"
