# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-08 07:17
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recepty', '0016_auto_20171208_0811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='komentar',
            name='publikovano',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 12, 8, 8, 17, 50, 147521)),
        ),
        migrations.AlterField(
            model_name='recept',
            name='hodnoceni',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=2),
        ),
        migrations.AlterField(
            model_name='recept',
            name='publikovano',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 12, 8, 8, 17, 50, 145520)),
        ),
    ]