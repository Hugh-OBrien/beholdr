from django.conf.urls import url

from iTunesReviews.views import main, runReport, search, progressPage

urlpatterns = [
    url(r'^$', main, name='main'),
    url(r'^report$', progressPage, name='progressPage'),
    url(r'^searchid$', search, name = 'search'),
]
