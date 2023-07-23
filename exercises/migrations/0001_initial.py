# Generated by Django 4.2.1 on 2023-07-23 19:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('chapters', '0002_alter_topic_is_extended'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exercise_content', models.TextField(help_text='Describe the content of exercise - the command', verbose_name='exercise content')),
                ('title', models.CharField(help_text='Title visible as exercise title in exercises list', max_length=255, verbose_name='exercise title')),
                ('is_extended', models.BooleanField(help_text='Should be checked if exercise belongs to the extended level', verbose_name='is extended')),
                ('topic', models.ForeignKey(help_text='The topic to which the exercise is linked', on_delete=django.db.models.deletion.CASCADE, to='chapters.topic', verbose_name='topic')),
            ],
            options={
                'verbose_name': 'exercise',
                'verbose_name_plural': 'exercises',
            },
        ),
    ]
