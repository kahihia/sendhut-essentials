# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-21 06:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lunch', '0007_auto_20180121_0600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='slug',
            field=models.CharField(max_length=240),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='slug',
            field=models.CharField(max_length=200),
        ),
    ]
