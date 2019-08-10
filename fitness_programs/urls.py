from django.conf.urls import url
from .views import fitness_program

urlpatterns = [ 
    url(r'^$', fitness_program, name='fitness_program'),

]