# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-08 11:30
from __future__ import unicode_literals

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recepty', '0033_auto_20171208_1218'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fotogalerie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazev', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='komentar',
            name='publikovano',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 12, 8, 12, 30, 51, 375180)),
        ),
        migrations.AlterField(
            model_name='recept',
            name='hodnoceni',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=3, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='recept',
            name='publikovano',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 12, 8, 12, 30, 51, 374680)),
        ),
    ]
