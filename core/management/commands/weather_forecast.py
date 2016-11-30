import arrow
import json
import requests
from django.conf import settings
from django.core.management.base import BaseCommand

from core.models import WeatherForecast


class Command(BaseCommand):
    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument('city', nargs='+', type=str)

        parser.add_argument(
            '--city',
            action='store_true',
            dest='city',
            default=False,
            help='Specify city',
        )

    API_16_DAYS_FORECAST_URL = 'http://api.openweathermap.org/data/2.5/forecast/daily?q={}&mode={}&units' \
                               '=metric&cnt={}&appid={}'

    def handle(self, *args, **options):
        city_name = options['city'][0]
        query = self.API_16_DAYS_FORECAST_URL.format(city_name, 'json', '14', settings.WEATHER_MAP_API_KEY)
        response = requests.get(query)
        response = json.loads(response.content)
        city = response['city']
        coord = city['coord']
        lat = coord['lat']
        lon = coord['lon']
        days_weather = response['list']
        for day_weather in days_weather:
            dt = day_weather['dt']
            today_date = arrow.get(dt).datetime
            clouds = day_weather['clouds']
            humidity = day_weather['humidity']
            wind_speed = day_weather['speed']
            cloudiness = day_weather['clouds']
            pressure = day_weather['pressure']
            weather = day_weather['weather']
            description = weather[0]['description']
            temp = day_weather['temp']
            temperature_min = temp['min']
            temperature_max = temp['max']
            temperature_eve = temp['eve']
            temperature_morn = temp['morn']
            temperature_night = temp['night']
            temperature_day = temp['day']
            WeatherForecast.objects.create(
                city=city_name,
                lat=lat,
                lon=lon,
                today_date=today_date,
                clouds=clouds,
                humidity=humidity,
                wind_speed=wind_speed,
                cloudiness=cloudiness,
                pressure=pressure,
                description=description,
                temperature_min=temperature_min,
                temperature_max=temperature_max,
                temperature_eve=temperature_eve,
                temperature_morn=temperature_morn,
                temperature_night=temperature_night,
                temperature_day=temperature_day
            )
            print 'YES'
