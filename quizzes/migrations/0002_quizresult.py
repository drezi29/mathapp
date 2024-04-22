# Generated by Django 4.1 on 2023-09-20 17:59

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quizzes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuizResult',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('score', models.IntegerField()),
                ('performing_datetime', models.DateTimeField(auto_now=True)),
                (
                    'quiz',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to='quizzes.quiz',
                        verbose_name='quiz',
                    ),
                ),
                (
                    'user',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                'verbose_name': 'Quiz Result',
                'verbose_name_plural': 'Quiz Results',
            },
        ),
    ]