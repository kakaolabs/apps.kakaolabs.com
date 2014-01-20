import json

from django_nose.testcases import FastFixtureTestCase

from kakaolabs.vendors.api.test.client import ApiClient
from kakaolabs.core.models import Member, App, Device


class TestDevice(FastFixtureTestCase):
    def setUp(self):
        self.member = Member.objects.create_member(
            'root', 'root@kakaolabs.com', 'a')
        self.app = App.objects.create(
            name='test', description='test', member=self.member)
        self.client = ApiClient(self.member.api_key, self.member.api_secret)

    def test_signup_with_new_device(self):
        old_count_devices = Device.objects.count()
        old_count_app_devices = self.app.devices.count()

        res = self.client.post('/v1/devices/signup/', params={
            'app_secret': self.app.app_secret
        }, data={
            'device_id': 'aaa',
            'device_type': 'ipod',
            'os': 0,
            'os_version': '7.0',
        })

        self.assertEqual(200, res.status_code)
        data = json.loads(res.content)

        new_count_devices = Device.objects.count()
        self.assertEqual(old_count_devices + 1, new_count_devices)

        new_count_devices = Device.objects.count()
        self.assertEqual(old_count_devices + 1, new_count_devices)

    def test_signup_with_old_device(self):
        Device.objects.create(token='aaa')

        old_count_devices = Device.objects.count()
        old_count_app_devices = self.app.devices.count()

        res = self.client.post('/v1/devices/signup/', params={
            'app_secret': self.app.app_secret
        }, data={
            'device_id': 'aaa',
            'device_type': 'ipod',
            'os': 0,
            'os_version': '7.0',
        })

        self.assertEqual(200, res.status_code)
        data = json.loads(res.content)

        new_count_devices = Device.objects.count()
        self.assertEqual(old_count_devices, new_count_devices)
