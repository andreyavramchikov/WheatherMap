from rest_framework import serializers

from core.models import WeatherForecast


class WeatherForecastSerializer(serializers.ModelSerializer):

    class Meta:
        model = WeatherForecast
        fields = '__all__'


class PressureSerializer(serializers.ModelSerializer):

    class Meta:
        model = WeatherForecast
        fields = ('pressure', 'today_date', )


class TemperatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherForecast
        fields = ('temperature_day', 'temperature_night', 'today_date',)

