from django.conf.urls import url
from .views import buy_program, payment

urlpatterns = [ 
    url(r'^$', buy_program, name='buy_program'),
    url(r'^payment', payment, name='payment'),

]