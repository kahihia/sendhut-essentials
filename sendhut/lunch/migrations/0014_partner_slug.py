# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-30 16:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lunch', '0013_partner_banner'),
    ]

    operations = [
        migrations.AddField(
            model_name='partner',
            name='slug',
            field=models.CharField(default=None, max_length=64),
            preserve_default=False,
        ),
    ]