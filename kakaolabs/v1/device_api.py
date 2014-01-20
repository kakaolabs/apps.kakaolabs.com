from kakaolabs.vendors.api.base import JsonApiController
from kakaolabs.vendors.api.decorators import serializer

from kakaolabs.core.models import Device, App
from kakaolabs.libs.authenticate import SignatureAuthenticate


class DeviceService(JsonApiController):
    authenticate_class = SignatureAuthenticate

    fields = (
        'access_token',
    )

    @serializer(fields)
    def post_signup(self, *args, **kwargs):
        app_secret = self.get_argument('app_secret', is_mandatory=True)
        device_id = self.get_post_argument('device_id', is_mandatory=True)
        device_type = self.get_post_argument('device_type', is_mandatory=True)
        os = int(self.get_post_argument('os', is_mandatory=True))
        os_version = self.get_post_argument('os_version', is_mandatory=True)

        app = App.objects.get(app_secret=app_secret)

        devices = Device.objects.filter(token=device_id)
        if devices.count() == 0:
            device = Device.objects.create(
                token=device_id, device_type=device_type,
                os=os, os_version=os_version)
        else:
            device = devies[0]
            Device.objects.filter(token=device_id).udpate(
                device_type=device_type, os=os, os_version=os_version)
        app.devices.add(device)

        return device
