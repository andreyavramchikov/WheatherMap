# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-30 09:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_weatherforecast_today_date'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='weatherforecast',
            unique_together=set([('today_date', 'city')]),
        ),
    ]
