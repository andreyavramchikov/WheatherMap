# Create your views here.
import arrow

from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import generics

from django.views.generic.base import TemplateView

from core.serializer import TemperatureSerializer
from .models import WeatherForecast
from .serializer import WeatherForecastSerializer, PressureSerializer


class HomeView(TemplateView):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        return super(HomeView, self).get(request, *args, **kwargs)


class GetForecastView(generics.ListAPIView):
    queryset = WeatherForecast.objects.all()
    serializer_class = WeatherForecastSerializer

    def get_queryset(self):
        queryset = super(GetForecastView, self).get_queryset()
        return queryset.filter(city=self.kwargs.get('city'))


class PressureDataView(generics.ListAPIView):
    queryset = WeatherForecast.objects.all()
    serializer_class = PressureSerializer

    def get_queryset(self):
        queryset = super(PressureDataView, self).get_queryset()
        two_week_after = arrow.now().replace(weeks=+2).datetime
        queryset = queryset.filter(city=self.kwargs.get('city'), today_date__lt=two_week_after,
                                   today_date__gte=arrow.now().datetime).values('pressure', 'today_date').order_by(
            'today_date')
        return queryset


class TemperatureDataView(generics.ListAPIView):
    queryset = WeatherForecast.objects.all()
    serializer_class = TemperatureSerializer

    def get_queryset(self):
        queryset = super(TemperatureDataView, self).get_queryset()
        two_week_after = arrow.now().replace(weeks=+2).datetime
        queryset = queryset.filter(city=self.kwargs.get('city'), today_date__lt=two_week_after,
                                   today_date__gte=arrow.now().datetime). \
            values('temperature_day', 'temperature_night', 'today_date', ).order_by('today_date')
        return queryset


class GetCoordinatesView(APIView):
    @staticmethod
    def get(request, *args, **kwargs):
        coorinates = WeatherForecast.objects.filter(city=kwargs['city']).values('lon', 'lat').first()
        return Response(coorinates)
