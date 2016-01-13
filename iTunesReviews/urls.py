from django.conf.urls import url

from iTunesReviews.views import main, runReport, search

urlpatterns = [
    url(r'^$', main, name='main'),
    url(r'^report$', runReport, name='runReport'),
    url(r'^search$', search, name = 'search'),
]
