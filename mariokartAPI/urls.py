"""mariokartAPI URL Configuration

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
from django.conf.urls import url
from django.contrib import admin

from mariokartAPI import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^games/$', views.games, name='game'),
    url(r'^games/(?P<pk>[0-9]+)/$', views.game, name='game-detail'),
    url(r'^circuits/$', views.circuits, name='circuit'),
    url(r'^circuits/(?P<pk>[0-9]+)/$', views.circuit, name='circuit-detail'),
    url(r'^characters/$', views.characters, name='character'),
    url(r'^characters/(?P<pk>[0-9]+)/$', views.character, name='character-detail'),
    url(r'^cups/$', views.cups, name='cup'),
    url(r'^cups/(?P<pk>[0-9]+)/$', views.cup, name='cup-detail'),

]
