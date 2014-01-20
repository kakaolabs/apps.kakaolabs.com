import json

from django_nose.testcases import FastFixtureTestCase

from kakaolabs.vendors.api.test.client import ApiClient
from kakaolabs.core.models import Member, App, Device, AppVersion


class TestApps(FastFixtureTestCase):
    def setUp(self):
        self.member = Member.objects.create_member(
            'root', 'root@kakaolabs.com', 'a')
        self.client = ApiClient(self.member.api_key, self.member.api_secret)

    def test_get_related(self):
        for i in xrange(10):
            App.objects.create(
                name='test%s' % i, description='test',
                member=self.member)
        res = self.client.get('/v1/apps/related/', params={'os': 0})
        self.assertEquals(200, res.status_code)
        data = json.loads(res.content)

        self.assertEquals(10, len(data))
        for item in data:
            self.assertEquals(
                sorted(['pk', 'name', 'description', 'image_url']),
                sorted(item.keys()))


class TestApp(FastFixtureTestCase):
    def setUp(self):
        self.member = Member.objects.create_member(
            'root', 'root@kakaolabs.com', 'a')
        self.client = ApiClient(self.member.api_key, self.member.api_secret)
        self.app = App.objects.create(
            name='test', description='test', member=self.member)


    def test_get_version(self):
        for i in xrange(0, 10):
            AppVersion.objects.create(app=self.app, version=1, subversion=i)

        res = self.client.get('/v1/app/%s/version/' % self.app.app_secret)
        self.assertEqual(200, res.status_code)
        data = json.loads(res.content)

        self.assertEquals(
                sorted(['version', 'subversion', 'is_force_update', 'download_url']),
                sorted(data.keys()))
        self.assertEquals(1, data['version'])
        self.assertEquals(9, data['subversion'])
