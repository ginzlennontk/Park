# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-26 02:00
from __future__ import unicode_literals

from django.db import migrations, models
import park.models


class Migration(migrations.Migration):

    dependencies = [
        ('park', '0004_auto_20170426_0155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to=park.models.path_and_rename),
        ),
    ]
