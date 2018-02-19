# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-19 10:04
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lunch', '0020_auto_20180218_2016'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='groupcart',
            name='alias',
        ),
        migrations.RemoveField(
            model_name='groupcart',
            name='recurring',
        ),
        migrations.AlterField(
            model_name='groupcart',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='group_carts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='groupcartmember',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='group_cart_memberships', to=settings.AUTH_USER_MODEL),
        ),
    ]