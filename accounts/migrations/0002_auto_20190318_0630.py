# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-18 06:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='occupation',
        ),
        migrations.AddField(
            model_name='user',
            name='handicap',
            field=models.CharField(default='', max_length=2),
        ),
        migrations.AddField(
            model_name='user',
            name='user_profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='static/images/profiles/', verbose_name='user_profile_picture'),
        ),
    ]