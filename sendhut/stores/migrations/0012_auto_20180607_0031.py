# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-07 00:31
from __future__ import unicode_literals

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0011_auto_20180507_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
