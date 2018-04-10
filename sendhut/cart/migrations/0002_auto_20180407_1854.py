# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-07 18:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='status',
            field=models.CharField(choices=[('open', 'Open - currently active'), ('canceled', 'Canceled - canceled by user'), ('locked', 'Locked - locked by user checkout')], default='open', max_length=32),
        ),
    ]