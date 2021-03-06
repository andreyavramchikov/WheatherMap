# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-29 11:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WeatherForecast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(blank=True, max_length=255)),
                ('lat', models.CharField(blank=True, max_length=255)),
                ('lon', models.CharField(blank=True, max_length=255)),
                ('clouds', models.CharField(blank=True, max_length=255)),
                ('humidity', models.CharField(blank=True, max_length=255)),
                ('wind_speed', models.CharField(blank=True, max_length=255)),
                ('cloudiness', models.CharField(blank=True, max_length=255)),
                ('pressure', models.CharField(blank=True, max_length=255)),
                ('description', models.CharField(blank=True, max_length=255)),
                ('temperature_min', models.CharField(blank=True, max_length=255)),
                ('temperature_max', models.CharField(blank=True, max_length=255)),
                ('temperature_eve', models.CharField(blank=True, max_length=255)),
                ('temperature_morn', models.CharField(blank=True, max_length=255)),
                ('temperature_night', models.CharField(blank=True, max_length=255)),
                ('temperature_day', models.CharField(blank=True, max_length=255)),
            ],
        ),
    ]
