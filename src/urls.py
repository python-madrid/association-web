from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('web.urls', namespace="web")),
    url(r'^', include('meetings.urls', namespace="meetings")),
    url(r'^ckeditor/', include('ckeditor.urls')),
)
