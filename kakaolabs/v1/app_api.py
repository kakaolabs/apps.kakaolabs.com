from kakaolabs.vendors.api.base import JsonApiController
from kakaolabs.vendors.api.decorators import serializer

from kakaolabs.core.models import Device, App
from kakaolabs.libs.authenticate import SignatureAuthenticate


class AppsService(JsonApiController):
    authenticate_class = SignatureAuthenticate

    fields = (
        'pk',
        'name',
        'description',
        'image_url',
    )

    @serializer(fields)
    def get_related(self, *args, **kwargs):
        apps = App.objects.filter(member=self.request.user)
        return apps
