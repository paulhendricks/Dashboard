# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-04 16:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashby', '0025_auto_20161003_1951'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]