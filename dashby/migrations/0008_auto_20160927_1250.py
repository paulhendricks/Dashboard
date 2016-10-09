# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-27 17:50
from __future__ import unicode_literals

import dashby.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashby', '0007_auto_20160927_1216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='document',
            field=models.FileField(upload_to='files/', validators=[dashby.validators.validate_file_type]),
        ),
    ]