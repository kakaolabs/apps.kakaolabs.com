from kakaolabs.vendors.api.base import JsonApiController, RestfulApiController
from kakaolabs.vendors.api.decorators import serializer

from kakaolabs.sms.models import Category, SMSContent
from kakaolabs.libs.authenticate import SignatureAuthenticate


class CategoriesService(RestfulApiController):
    authenticate_class = SignatureAuthenticate

    fields = (
        'id',
        'name',
        'image_url',
        'index',
        'type',
        ('data', ('id', 'name', 'type', 'image_url', 'index')),
    )

    @serializer(fields)
    def get(self, *args, **kwargs):
        epoch_time = self.get_argument('time', is_mandatory=True)

        categories = Category.objects.filter(parent=None).order_by('index', 'name')
        return categories


class SubcategoryService(RestfulApiController):
    authenticate_class = SignatureAuthenticate

    fields = (
        'id',
        'content',
        'index',
        'votes',
    )

    @serializer(fields)
    def get(self, category_id):
        epoch_time = self.get_argument('time', is_mandatory=True)
        size = int(self.get_argument('size', default_value=50))
        offset = int(self.get_argument('offset', default_value=0))

        data_size = SMSContent.objects.filter(category__pk=category_id).count()
        min_index = min(offset, data_size)
        max_index = min(offset + size, data_size)
        data = SMSContent.objects.filter(category__pk=category_id).order_by('index', 'content')[min_index:max_index]
        return data
