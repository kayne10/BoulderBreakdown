# -*- coding: utf-8 -*-
# Generated by Django 1.10b1 on 2016-09-21 15:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0006_auto_20160913_2249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='forum_comment',
            field=models.TextField(max_length=1000),
        ),
    ]