# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-29 14:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashby', '0014_docs'),
    ]

    operations = [
        migrations.RenameField(
            model_name='document',
            old_name='document',
            new_name='file',
        ),
    ]
