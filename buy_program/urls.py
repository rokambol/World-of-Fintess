from django.conf.urls import url
from .views import buy_program, your_details

urlpatterns = [ 
    url(r'^$', buy_program, name='buy_program'),
    url(r'^your_details', your_details, name='your_details'),
]