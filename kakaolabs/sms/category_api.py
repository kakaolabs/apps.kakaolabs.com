from kakaolabs.vendors.api.base import JsonApiController, RestfulApiController
from kakaolabs.vendors.api.decorators import serializer

from kakaolabs.sms.models import Category, SMSContent
from kakaolabs.libs.authenticate import SignatureAuthenticate


class CategoriesService(RestfulApiController):
    authenticate_class = SignatureAuthenticate

    fields = (
        'id',
        'name',
        'type',
        ('data', ('id', 'name', 'type')),
    )

    @serializer(fields)
    def get(self, *args, **kwargs):
        categories = Category.objects.filter(parent=None)
        return categories


class SubcategoryService(RestfulApiController):
    authenticate_class = SignatureAuthenticate

    fields = (
        'id',
        'content',
        'votes',
    )

    @serializer(fields)
    def get(self, category_id):
        data = SMSContent.objects.filter(category__pk=category_id)
        return data
