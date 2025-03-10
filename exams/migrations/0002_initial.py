# Generated by Django 5.1.5 on 2025-02-22 12:00

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('exams', '0001_initial'),
        ('quizzes', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='studentanswer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_answers', to='quizzes.question'),
        ),
        migrations.AddField(
            model_name='studentanswer',
            name='selected_choice',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='student_answers', to='quizzes.choice'),
        ),
        migrations.AddField(
            model_name='testsession',
            name='quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='test_sessions', to='quizzes.quiz'),
        ),
        migrations.AddField(
            model_name='testsession',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='test_sessions', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='testresult',
            name='session',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='result', to='exams.testsession'),
        ),
        migrations.AddField(
            model_name='studentanswer',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='exams.testsession'),
        ),
    ]
