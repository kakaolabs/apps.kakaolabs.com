from django.db import models

from kakaolabs.libs import utils
from kakaolabs.core.models import os_model


class Device(models.Model):
    class Meta:
        app_label = 'core'

    token =  models.CharField(max_length=200, unique=True, db_index=True, null=True)
    device_type = models.CharField(max_length=100, db_index=True)
    os = models.SmallIntegerField(choices=os_model.DEVICE_OS_CHOICES, default=os_model.IOS, db_index=True)
    os_version = models.CharField(max_length=20, db_index=True)
    access_token = models.CharField(max_length=60, default=utils.generate_uuid)
    created = models.DateTimeField(auto_now_add=True, db_index=True)
