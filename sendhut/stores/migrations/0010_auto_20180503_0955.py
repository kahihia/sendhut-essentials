# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-03 09:55
from __future__ import unicode_literals

from decimal import Decimal
import django.contrib.postgres.fields
from django.db import migrations, models
import djmoney.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0009_auto_20180410_0100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='categories',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(choices=[('local-gems', 'Local gems'), ('halal', 'Halal'), ('vegetarian', 'Vegetarian'), ('dessert-sweets', 'Desserts'), ('dessert-sweets', 'Sweet treats'), ('guilty-pleasures', 'guilty pleasures'), ('bakery', 'Bakery'), ('fresh-juice', 'Fresh Juice'), ('healthy-food', 'Healthy Food')]), blank=True, default=list, size=None),
        ),
        migrations.AlterField(
            model_name='item',
            name='dietary_labels',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(choices=[('gluten-free', 'Gluten Free'), ('dairy-free', 'Dairy Free'), ('vegan', 'Vegan'), ('vegetarian', 'Vegetarian'), ('halal', 'Halal')]), blank=True, default=list, size=None),
        ),
    ]