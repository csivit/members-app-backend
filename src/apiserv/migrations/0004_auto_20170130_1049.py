# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-30 10:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiserv', '0003_auto_20170130_0950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='members',
            name='password',
            field=models.CharField(max_length=65),
        ),
        migrations.AlterField(
            model_name='members',
            name='regno',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]