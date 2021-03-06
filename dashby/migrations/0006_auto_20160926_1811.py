# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-26 18:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dashby', '0005_auto_20160926_1743'),
    ]

    operations = [
        migrations.RenameField(
            model_name='document',
            old_name='docfile',
            new_name='document',
        ),
        migrations.AddField(
            model_name='document',
            name='description',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='document',
            name='uploaded_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
