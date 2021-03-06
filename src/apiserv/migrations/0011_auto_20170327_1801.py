# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-27 18:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiserv', '0010_auto_20170301_1250'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='short_desc',
            field=models.CharField(default='New CSI EVENT', max_length=80),
        ),
        migrations.AlterField(
            model_name='event',
            name='images',
            field=models.ImageField(default='images/no-img.jpg', upload_to='images/'),
        ),
    ]
