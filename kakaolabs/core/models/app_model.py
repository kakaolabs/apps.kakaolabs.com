from django.db import models

from kakaolabs.libs import utils


class App(models.Model):
    class Meta:
        app_label = 'core'

    member = models.ForeignKey('Member', related_name='apps')
    name = models.CharField(max_length=200)
    description = models.TextField()
    image_url = models.URLField(null=True, blank=True)
    devices = models.ManyToManyField('Device', blank=True)
    app_secret = models.CharField(max_length=60, default=utils.generate_uuid)
