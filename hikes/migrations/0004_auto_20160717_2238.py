# -*- coding: utf-8 -*-
# Generated by Django 1.10b1 on 2016-07-17 22:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hikes', '0003_hike_hike_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hike',
            name='hike_image',
            field=models.FileField(upload_to=b''),
        ),
    ]
