# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-16 18:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('overview', '0013_candidate_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='cpf_id',
            field=models.IntegerField(null=True),
        ),
    ]
