# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Category.image_url'
        db.add_column(u'sms_category', 'image_url',
                      self.gf('django.db.models.fields.URLField')(default='http://static.appota.com/uploads/icon/112013/thumbs/icon6.png', max_length=200),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Category.image_url'
        db.delete_column(u'sms_category', 'image_url')


    models = {
        u'sms.category': {
            'Meta': {'ordering': "['index', 'name']", 'object_name': 'Category'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_url': ('django.db.models.fields.URLField', [], {'default': "'http://static.appota.com/uploads/icon/112013/thumbs/icon6.png'", 'max_length': '200'}),
            'index': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['sms.Category']"}),
            'type': ('django.db.models.fields.SmallIntegerField', [], {'default': '1', 'db_index': 'True'})
        },
        u'sms.smscontent': {
            'Meta': {'ordering': "['index', '-votes']", 'object_name': 'SMSContent'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sms'", 'to': u"orm['sms.Category']"}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'}),
            'votes': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'})
        }
    }

    complete_apps = ['sms']