# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-09 17:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20170609_1619'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='cover',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='game',
            name='released_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
