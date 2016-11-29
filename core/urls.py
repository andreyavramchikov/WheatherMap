from django.conf.urls import url

from .views import HomeView, GetForecastView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^api/forecast/$', GetForecastView.as_view(), name='data'),
    # url(r'^api/data/$', GetForecastDataView.as_view(), name='data'),
    # url(r'^$', HomeView.as_view(), name='home'),
    # url(r'^contact/$', ContactUsView.as_view(), name='contact'),
]