from django.conf.urls import url, include
from .views import all_exercises

urlpatterns = [
    url(r'^$', all_exercises, name='exercises')
    ]