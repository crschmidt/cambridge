# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-07 01:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('overview', '0016_auto_20170806_2025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='logo',
            field=models.URLField(blank=True, max_length=150),
        ),
    ]
