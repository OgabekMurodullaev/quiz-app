from django.db import models

from users.models import User


class Group(models.Model):
    name = models.CharField(max_length=10)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='teaching_groups')
    student = models.ManyToManyField(User, related_name="student_groups")

    def __str__(self):
        return f"Group name: {self.name}, Teacher: {self.teacher}"

    class Meta:
        verbose_name = "Group"
        verbose_name_plural = "Groups"
