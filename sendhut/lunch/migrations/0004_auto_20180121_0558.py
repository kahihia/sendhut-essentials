# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-21 05:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lunch', '0003_auto_20180121_0555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='info',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]