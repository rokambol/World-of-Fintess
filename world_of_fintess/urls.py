"""world_of_fintess URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from accounts import urls as urls_accounts
from exercises import urls as urls_exercises
from buy_program import urls as urls_buy_program
from fitness_programs import urls as urls_fitness_program
from search import urls as urls_search
from exercises.views import all_exercises, single_exercise
from django.views import static
from .settings import MEDIA_ROOT


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', all_exercises, name='index'),
    url(r'^accounts/', include(urls_accounts)),
    url(r'^search/', include(urls_search)),
    url(r'^exercises/', include(urls_exercises)),
    url(r'^single_exercise/', include(urls_exercises)),
    url(r'^buy_program/', include(urls_buy_program)),
    url(r'^fitness_programs/', include(urls_fitness_program)),
    url(r'^media/(?P<path>.*)$', static.serve, {'document_root': MEDIA_ROOT}),
]
