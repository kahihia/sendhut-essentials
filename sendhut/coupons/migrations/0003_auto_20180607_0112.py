# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-07 01:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coupons', '0002_auto_20180607_0041'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CampaignDropoffs',
            new_name='CampaignDropoff',
        ),
        migrations.AlterModelTable(
            name='campaigndropoff',
            table='campaign_dropoff',
        ),
    ]
