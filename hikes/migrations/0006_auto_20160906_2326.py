# -*- coding: utf-8 -*-
# Generated by Django 1.10b1 on 2016-09-06 23:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hikes', '0005_hike_hike_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hike',
            name='hike_description',
            field=models.TextField(max_length=2000),
        ),
    ]