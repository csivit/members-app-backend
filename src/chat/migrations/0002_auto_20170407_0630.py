# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-07 06:30
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='users',
            field=models.ManyToManyField(related_name='users_arr', to=settings.AUTH_USER_MODEL),
        ),
    ]