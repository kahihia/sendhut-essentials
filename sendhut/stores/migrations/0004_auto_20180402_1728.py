# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-02 17:28
from __future__ import unicode_literals

from django.db import migrations
import djmoney.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0003_auto_20180331_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='option',
            name='price',
            field=djmoney.models.fields.MoneyField(blank=True, decimal_places=2, default=None, max_digits=10, null=True),
        ),
    ]
