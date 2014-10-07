from django.conf.urls import patterns, url

from .views import HomeView, RedirectPostView


urlpatterns = patterns('',
    url(r'^post/(?P<slug>[\w\d\-]+)/$', RedirectPostView.as_view(), name='redirect-post'),
    url(r'^$', HomeView.as_view(), name='home'),
)
