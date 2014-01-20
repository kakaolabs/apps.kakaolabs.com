# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'AppVersion.is_force_update'
        db.add_column(u'core_appversion', 'is_force_update',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'AppVersion.is_force_update'
        db.delete_column(u'core_appversion', 'is_force_update')


    models = {
        'core.app': {
            'Meta': {'object_name': 'App'},
            'app_secret': ('django.db.models.fields.CharField', [], {'default': "'088ef449-897d-45e4-a5a3-88a985ddb5ed'", 'max_length': '60'}),
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
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'device_type': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'os': ('django.db.models.fields.SmallIntegerField', [], {'default': '0', 'db_index': 'True'}),
            'os_version': ('django.db.models.fields.CharField', [], {'max_length': '20', 'db_index': 'True'}),
            'token': ('django.db.models.fields.CharField', [], {'max_length': '200', 'unique': 'True', 'null': 'True', 'db_index': 'True'})
        },
        'core.member': {
            'Meta': {'object_name': 'Member'},
            'api_key': ('django.db.models.fields.CharField', [], {'default': "'603dd0a5-4dc7-400c-b007-76e79d2c95be'", 'max_length': '60'}),
            'api_secret': ('django.db.models.fields.CharField', [], {'default': "'e72f6c3f-81ad-42fd-a876-5db31a61b014'", 'max_length': '60'}),
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