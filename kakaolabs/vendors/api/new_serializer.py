from datetime import datetime
from django.db.models.query import QuerySet
from django.utils.encoding import smart_str
from django.db import models


class AbstractPresenter():
    def get_fields(self, obj):
        if isinstance(obj, models.Model):
            return tuple(obj._meta.fields)
        elif type(obj) == dict:
            return tuple(obj.keys())
        elif type(obj) == list:
            if obj:
                return self.get_fields(obj[0])
            else:
                return []

    def get_attr(self, obj, field, is_list=False, is_tuple=False):
        try:
            data = obj[field] if type(obj) == dict else getattr(obj, field)
            if isinstance(data, datetime):
                return smart_str(data)
            return data
        except:
            if is_tuple:
                return {}
            elif is_list:
                return []
            else:
                return ""

    def render(self, obj, fields=None):
        fields = self.get_fields(obj) if not fields else fields
        if not fields:
            return {} if type(obj) != list else []

        if isinstance(obj, models.Manager):
            return self.render_query_manager(obj, fields)
        elif type(obj) == list or isinstance(obj, QuerySet):
            return self.render_list(obj, fields)
        else:
            return self.render_obj(obj, fields)

    def render_obj(self, obj, fields):
        data = {}
        for field in fields:
            self.render_field(data, obj, field)
        return data

    def render_field(self, data, obj, field):
        if type(field) == list:
            subfield = field[0]
            fields = field[1]
            new_obj = self.get_attr(obj, subfield, is_list=True)
            if isinstance(new_obj, models.Manager):
                data[subfield] = self.render_query_manager(new_obj, fields)
            else:
                data[subfield] = self.render_list(new_obj, fields)
        elif type(field) == tuple:
            subfield = field[0]
            fields = field[1]
            new_obj = self.get_attr(obj, subfield, is_tuple=True)
            data[subfield] = self.render(new_obj, fields)
        else:
            data[field] = self.get_attr(obj, field)

    def render_list(self, objs, fields):
        data = []
        for obj in objs:
            data.append(self.render(obj, fields))
        return data

    def render_query_manager(self, objs, fields):
        data = []
        for obj in objs.all():
            data.append(self.render(obj, fields))
        return data


class Serializer(object):
    def __init__(self, fields):
        self.fields = fields

    def serialize(self, obj):
        return AbstractPresenter().render(obj, self.fields)
