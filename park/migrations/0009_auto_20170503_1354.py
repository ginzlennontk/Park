# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-03 13:54
from __future__ import unicode_literals

from django.db import migrations, models
import park.models


class Migration(migrations.Migration):

    dependencies = [
        ('park', '0008_auto_20170503_1332'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animal',
            name='picture',
        ),
        migrations.AlterField(
            model_name='animalimage',
            name='image',
            field=models.ImageField(upload_to=park.models.path_and_rename),
        ),
    ]
