# Generated by Django 5.1.5 on 2025-02-08 10:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0003_rename_group_quiz_groups'),
    ]

    operations = [
        migrations.DeleteModel(
            name='StudentAnswer',
        ),
    ]
