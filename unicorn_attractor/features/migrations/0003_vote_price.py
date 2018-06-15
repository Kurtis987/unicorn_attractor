# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-15 16:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0002_feature_current_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='vote',
            name='price',
            field=models.DecimalField(decimal_places=2, default=5.0, max_digits=6),
        ),
    ]