# Generated by Django 2.2 on 2020-11-07 04:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20201106_1044'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='students',
            name='total',
        ),
    ]
