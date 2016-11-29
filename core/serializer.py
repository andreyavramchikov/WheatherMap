from rest_framework import serializers

from core.models import WeatherForecast


class WeatherForecastSerializer(serializers.ModelSerializer):

    class Meta:
        model = WeatherForecast
        fields = '__all__'