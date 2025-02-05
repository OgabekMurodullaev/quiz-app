from django.contrib.auth.models import AbstractUser
from django.db import models

from users.managers import UserManager


class User(AbstractUser):
    USER_TYPE = (
        ('student', 'Student'),
        ('teacher', 'Teacher'),
    )

    user_type = models.CharField(max_length=8, choices=USER_TYPE, default='student')
    objects = UserManager()

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.user_type}"

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']


