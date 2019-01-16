# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-08 07:42
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recepty', '0021_auto_20171208_0829'),
    ]

    operations = [
        migrations.RenameField(
            model_name='kuchar',
            old_name='kuchar',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='kuchar',
            name='jmeno',
        ),
        migrations.AlterField(
            model_name='komentar',
            name='publikovano',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 12, 8, 8, 42, 31, 721140)),
        ),
        migrations.AlterField(
            model_name='recept',
            name='publikovano',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 12, 8, 8, 42, 31, 719139)),
        ),
    ]
