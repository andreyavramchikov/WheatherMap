# Create your views here.
from rest_framework import generics

from django.views.generic.base import TemplateView

from .models import WeatherForecast
from .serializer import WeatherForecastSerializer


class HomeView(TemplateView):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        return super(HomeView, self).get(request, *args, **kwargs)


class GetForecastView(generics.ListCreateAPIView):
    queryset = WeatherForecast.objects.all()
    serializer_class = WeatherForecastSerializer
    page_size = 100

    def get_queryset(self):
        queryset = super(GetForecastView, self).get_queryset()
        return queryset