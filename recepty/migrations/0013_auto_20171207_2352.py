# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-07 22:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recepty', '0012_recept_hodnoceni'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recept',
            name='hodnoceni',
            field=models.IntegerField(default=2.5),
        ),
    ]
