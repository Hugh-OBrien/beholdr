from django.conf.urls import url

from simple_cast.views import listenByEpisode

urlpatterns = [
    url(r'^$', listenByEpisode, name='listenByEpisode'),
]
