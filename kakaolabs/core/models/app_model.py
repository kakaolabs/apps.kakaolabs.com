from django.db import models

from kakaolabs.libs import utils


class App(models.Model):
    class Meta:
        app_label = 'core'

    member = models.ForeignKey('Member', related_name='apps')
    name = models.CharField(max_length=200)
    description = models.TextField()
    image_url = models.URLField(null=True, blank=True)
    app_secret = models.CharField(max_length=60, default=utils.generate_uuid)
    devices = models.ManyToManyField('Device', blank=True)
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    @property
    def newest_version(self):
        from .appversion_model import AppVersion
        if self.versions.count():
            return self.versions.order_by('-version', '-subversion')[0]
        else:
            return {}

    def __unicode__(self):
        return self.name
