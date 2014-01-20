# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Device.access_token'
        db.add_column(u'core_device', 'access_token',
                      self.gf('django.db.models.fields.CharField')(default='ac0f12de-b929-47c3-b80c-f7afd6b06b84', max_length=60),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Device.access_token'
        db.delete_column(u'core_device', 'access_token')


    models = {
        'core.app': {
            'Meta': {'object_name': 'App'},
            'app_secret': ('django.db.models.fields.CharField', [], {'default': "'1521e887-de5b-4b01-b47b-6bd5e8d976fd'", 'max_length': '60'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'devices': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['core.Device']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'member': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'apps'", 'to': "orm['core.Member']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'core.appversion': {
            'Meta': {'object_name': 'AppVersion'},
            'app': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'apps'", 'to': "orm['core.App']"}),
            'download_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_force_update': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'os': ('django.db.models.fields.SmallIntegerField', [], {'default': '0', 'db_index': 'True'}),
            'subversion': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'version': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'})
        },
        'core.device': {
            'Meta': {'object_name': 'Device'},
            'access_token': ('django.db.models.fields.CharField', [], {'default': "'e234832e-f5c4-4b14-a6ec-b483f5e47f95'", 'max_length': '60'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'device_type': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'os': ('django.db.models.fields.SmallIntegerField', [], {'default': '0', 'db_index': 'True'}),
            'os_version': ('django.db.models.fields.CharField', [], {'max_length': '20', 'db_index': 'True'}),
            'token': ('django.db.models.fields.CharField', [], {'max_length': '200', 'unique': 'True', 'null': 'True', 'db_index': 'True'})
        },
        'core.member': {
            'Meta': {'object_name': 'Member'},
            'api_key': ('django.db.models.fields.CharField', [], {'default': "'4d91bbd1-cb5a-49c0-abe7-1510506c8d5f'", 'max_length': '60'}),
            'api_secret': ('django.db.models.fields.CharField', [], {'default': "'2161cb3f-050e-4c97-a66a-02032f1160bd'", 'max_length': '60'}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '254', 'unique': 'True', 'null': 'True', 'db_index': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_admin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '200', 'unique': 'True', 'null': 'True', 'db_index': 'True'})
        }
    }

    complete_apps = ['core']