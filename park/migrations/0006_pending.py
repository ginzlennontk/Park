# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-01 02:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('park', '0005_auto_20170426_0200'),
    ]

    operations = [
        migrations.CreateModel(
            name='pending',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thai_name', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('class_name', models.CharField(max_length=200)),
                ('order', models.CharField(max_length=200)),
                ('family', models.CharField(max_length=200)),
                ('info', models.TextField(blank=True, null=True)),
                ('habitat', models.TextField(blank=True, null=True)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='pending_pic/')),
            ],
        ),
    ]
