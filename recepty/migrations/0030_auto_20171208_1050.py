# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-08 09:50
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recepty', '0029_auto_20171208_1026'),
    ]

    operations = [
        migrations.AddField(
            model_name='svetovakuchyne',
            name='popis',
            field=models.TextField(default='popis', max_length=1000),
        ),
        migrations.AlterField(
            model_name='komentar',
            name='publikovano',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 12, 8, 10, 50, 8, 824364)),
        ),
        migrations.AlterField(
            model_name='komentar',
            name='text',
            field=models.TextField(default='text', max_length=300),
        ),
        migrations.AlterField(
            model_name='recept',
            name='postup',
            field=models.TextField(default='postup', max_length=2000),
        ),
        migrations.AlterField(
            model_name='recept',
            name='publikovano',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 12, 8, 10, 50, 8, 823363)),
        ),
    ]
