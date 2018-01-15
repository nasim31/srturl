# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-01-06 17:15
from __future__ import unicode_literals

from django.db import migrations, models
import shortener.validators


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0005_auto_20180102_0146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='srturl',
            name='url',
            field=models.URLField(validators=[shortener.validators.validate_url]),
        ),
    ]