# Generated by Django 5.1.5 on 2025-02-06 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='text',
            field=models.CharField(max_length=150),
        ),
    ]
