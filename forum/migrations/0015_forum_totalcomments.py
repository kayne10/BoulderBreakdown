# -*- coding: utf-8 -*-
# Generated by Django 1.10b1 on 2016-10-03 01:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0014_auto_20161002_2152'),
    ]

    operations = [
        migrations.AddField(
            model_name='forum',
            name='totalComments',
            field=models.IntegerField(default=0),
        ),
    ]
