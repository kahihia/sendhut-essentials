# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-11 17:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('giveaways', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupon',
            name='redeemed_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
