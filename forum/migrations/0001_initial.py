# -*- coding: utf-8 -*-
# Generated by Django 1.10b1 on 2016-07-21 17:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Forum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_title', models.CharField(max_length=250)),
                ('article_subject', models.CharField(max_length=250)),
                ('article_body', models.CharField(max_length=2000)),
            ],
        ),
    ]