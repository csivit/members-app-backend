# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-01 12:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiserv', '0009_auto_20170215_1300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='images',
            field=models.ImageField(default='images/no-img.jpg', upload_to='static/'),
        ),
    ]
