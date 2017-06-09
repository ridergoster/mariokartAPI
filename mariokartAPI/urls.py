from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^login/$', views.login, name='login'),
    url(r'^users/$', views.users, name='user'),
    url(r'^admin/', admin.site.urls),
    url(r'^games/$', views.games, name='game'),
    url(r'^games/(?P<pk>[0-9]+)/$', views.game, name='game-detail'),
    url(r'^circuits/$', views.circuits, name='circuit'),
    url(r'^circuits/(?P<pk>[0-9]+)/$', views.circuit, name='circuit-detail'),
    url(r'^characters/$', views.characters, name='character'),
    url(r'^characters/(?P<pk>[0-9]+)/$', views.character, name='character-detail'),
    url(r'^cups/$', views.cups, name='cup'),
    url(r'^cups/(?P<pk>[0-9]+)/$', views.cup, name='cup-detail'),
    url(r'^statistics/$', views.statistics, name='statistic'),
    url(r'^statistics/(?P<pk>[0-9]+)/$', views.statistic, name='statistic-detail'),
]
