from django.conf.urls import patterns, url

from .views import MeetingsView, MeetingView


urlpatterns = patterns('',
    url(r'^meetings/(?P<slug>[\w\d\-]+)/$', MeetingView.as_view(), name='meeting'),
    url(r'^meetings/$', MeetingsView.as_view(), name='meetings')
)
