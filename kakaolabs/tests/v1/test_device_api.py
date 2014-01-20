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

    def test_signup(self):
        res = self.client.post('/v1/devices/signup/', params={
            'app_secret': self.app.app_secret
        }, data={
            'device_id': 'aaa',
            'device_type': 'ipod',
            'os': 0,
            'os_version': '7.0',
        })

        self.assertEquals(200, res.status_code)
        data = json.loads(res.content)
