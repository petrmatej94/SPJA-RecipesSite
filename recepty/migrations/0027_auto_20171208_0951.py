# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-08 08:51
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recepty', '0026_auto_20171208_0951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='komentar',
            name='publikovano',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 12, 8, 9, 51, 22, 124806)),
        ),
        migrations.AlterField(
            model_name='recept',
            name='publikovano',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 12, 8, 9, 51, 22, 123805)),
        ),
    ]