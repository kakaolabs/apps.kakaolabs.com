from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^v1/', include('v1.urls')),
    url(r'^sms/', include('sms.urls')),
)


urlpatterns += staticfiles_urlpatterns()
