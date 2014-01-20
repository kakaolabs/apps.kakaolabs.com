import json

from django_nose.testcases import FastFixtureTestCase

from kakaolabs.vendors.api.test.client import ApiClient
from kakaolabs.core.models import Member, App, Device


class TestApp(FastFixtureTestCase):
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
