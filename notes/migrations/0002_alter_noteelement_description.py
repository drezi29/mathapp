# Generated by Django 4.2.1 on 2023-07-04 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noteelement',
            name='description',
            field=models.CharField(blank=True, help_text='Title that can be placed below content on the template to describe content', max_length=255, null=True, verbose_name='description'),
        ),
    ]