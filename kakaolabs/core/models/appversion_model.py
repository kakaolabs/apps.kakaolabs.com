from django.db import models

from kakaolabs.core.models import os_model


class AppVersion(models.Model):
    class Meta:
        app_label = 'core'

    app = models.ForeignKey('App', related_name='apps')
    os = models.SmallIntegerField(choices=os_model.DEVICE_OS_CHOICES, default=os_model.IOS, db_index=True)
    is_force_update = models.BooleanField(default=False)
    version = models.SmallIntegerField(default=0)
    subversion = models.SmallIntegerField(default=0)
    download_url = models.URLField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
