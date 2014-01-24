import json

from django_nose.testcases import FastFixtureTestCase

from kakaolabs.vendors.api.test.client import ApiClient
from kakaolabs.sms.models import SMSContent, Category
from kakaolabs.core.models import Member


class TestCategory(FastFixtureTestCase):
    def setUp(self):
        self.member = Member.objects.create_member(
            'root', 'root@kakaolabs.com', 'a')
        self.client = ApiClient(self.member.api_key, self.member.api_secret)

    def test_get_categories(self):
        cat = Category.objects.create(name='test', type=Category.CATEGORY)
        for i in xrange(5):
            Category.objects.create(
                name='subtest-%s' % i, type=Category.SUBCATEGORY, parent=cat)

        res = self.client.get('/sms/v1/categories/')
        self.assertEquals(200, res.status_code)
        data = json.loads(res.content)

        self.assertEqual(1, len(data))
        cate = data[0]
        self.assertEqual(
            sorted(['id', 'name', 'type', 'data', 'image_url', 'index']),
            sorted(cate.keys()))
        subcates = cate['data']
        self.assertEqual(5, len(subcates))
        for item in subcates:
            self.assertEqual(
                sorted(['id', 'name', 'type', 'image_url', 'index']),
                sorted(item.keys()))


class TestSubCategory(FastFixtureTestCase):
    def setUp(self):
        self.member = Member.objects.create_member(
            'root', 'root@kakaolabs.com', 'a')
        self.client = ApiClient(self.member.api_key, self.member.api_secret)

    def test_get_categories(self):
        cat = Category.objects.create(name='test', type=Category.SUBCATEGORY)
        for i in xrange(5):
            SMSContent.objects.create(
                content='content-%i' % i, votes=i, category=cat)

        res = self.client.get('/sms/v1/subcategory/%s/' % cat.pk)
        self.assertEquals(200, res.status_code)
        data = json.loads(res.content)

        self.assertEqual(5, len(data))
        for item in data:
            self.assertEqual(
                sorted(['id', 'content', 'votes', 'index']),
                sorted(item.keys()))

