from django.conf.urls import patterns, url

from .device_api import DeviceService
from .app_api import AppsService


urlpatterns = patterns('',
    url(r'^devices/(?P<action>\w+)/$', DeviceService.as_view()),
    url(r'^apps/(?P<action>\w+)/$', AppsService.as_view()),
)
