from django.conf.urls import url

from iTunesReviews.views import main, runReport

urlpatterns = [
    url(r'^$', main, name='main'),
    url(r'^/report$', runReport, name='runReport'),
]