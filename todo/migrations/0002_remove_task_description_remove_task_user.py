# Generated by Django 4.1.6 on 2023-02-09 19:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='description',
        ),
        migrations.RemoveField(
            model_name='task',
            name='user',
        ),
    ]
