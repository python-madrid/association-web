from django.conf.urls import patterns, url

from .views import MeetingsView


urlpatterns = patterns('',
    url(r'^meetings/$', MeetingsView.as_view(), name='meetings')
)
