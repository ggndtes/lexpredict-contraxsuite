# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-31 16:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extract', '0005_auto_20170810_2015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='court',
            name='abbreviation',
            field=models.CharField(blank=True, db_index=True, max_length=50),
        ),
    ]