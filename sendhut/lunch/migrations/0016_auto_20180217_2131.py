# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-17 21:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lunch', '0015_vendor_verified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupcart',
            name='order',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='group_cart', to='lunch.Order'),
        ),
    ]
