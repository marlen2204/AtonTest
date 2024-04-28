from django.urls import include, path
from .views import index, calculate_exchange_rates


app_name = 'valute'


urlpatterns = [
    path('',
         index,
         name='index'),
    path('calculate_exchange_rates/',
         calculate_exchange_rates,
         name='calculate_exchange_rates'),
]
