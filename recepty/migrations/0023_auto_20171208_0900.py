# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-08 08:00
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recepty', '0022_auto_20171208_0842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='komentar',
            name='publikovano',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 12, 8, 9, 0, 14, 865639)),
        ),
        migrations.AlterField(
            model_name='recept',
            name='publikovano',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 12, 8, 9, 0, 14, 863637)),
        ),
    ]
