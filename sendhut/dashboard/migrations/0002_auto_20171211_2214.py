# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-11 22:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allowance',
            name='name',
            field=models.CharField(blank=True, default='DimGray-Crosby-Circle', max_length=100, null=True),
        ),
    ]
