from django.conf.urls import url, include
from .views import all_exercises, single_exercise

urlpatterns = [
    url(r'^$', all_exercises, name='exercises'),
    url(r'^single_exercise/(?P<exercise_id>[0-9]+)/$', single_exercise, name='single_exercise')
    ]