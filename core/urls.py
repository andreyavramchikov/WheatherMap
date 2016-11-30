from django.conf.urls import url

from .views import HomeView, GetForecastView, PressureDataView, TemperatureDataView, GetCoordinatesView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^api/(?P<city>[\w\-]+)/pressure/$', PressureDataView.as_view(), name='pressure'),
    url(r'^api/(?P<city>[\w\-]+)/temperature/$', TemperatureDataView.as_view(), name='temperature'),
    url(r'^api/(?P<city>[\w\-]+)/forecast/$', GetForecastView.as_view(), name='forecast'),
    url(r'^api/(?P<city>[\w\-]+)/$', GetCoordinatesView.as_view(), name='coordinates'),
]