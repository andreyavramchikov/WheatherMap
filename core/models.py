from __future__ import unicode_literals

from django.db import models

# Create your models here.


class WeatherForecast(models.Model):
    city = models.CharField(max_length=255, blank=True)
    lat = models.CharField(max_length=255, blank=True)
    lon = models.CharField(max_length=255, blank=True)
    today_date = models.DateField()
    clouds = models.CharField(max_length=255, blank=True)
    humidity = models.CharField(max_length=255, blank=True)
    wind_speed = models.CharField(max_length=255, blank=True)
    cloudiness = models.CharField(max_length=255, blank=True)
    pressure = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True)
    temperature_min = models.CharField(max_length=255, blank=True)
    temperature_max = models.CharField(max_length=255, blank=True)
    temperature_eve = models.CharField(max_length=255, blank=True)
    temperature_morn = models.CharField(max_length=255, blank=True)
    temperature_night = models.CharField(max_length=255, blank=True)
    temperature_day = models.CharField(max_length=255, blank=True)
