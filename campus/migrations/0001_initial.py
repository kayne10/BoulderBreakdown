# -*- coding: utf-8 -*-
# Generated by Django 1.10b1 on 2016-09-12 02:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CampusObject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description_url', models.CharField(max_length=200)),
            ],
        ),
    ]
