# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Member.first_name'
        db.add_column(u'core_member', 'first_name',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=60),
                      keep_default=False)

        # Adding field 'Member.last_name'
        db.add_column(u'core_member', 'last_name',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=60),
                      keep_default=False)

        # Adding unique constraint on 'Member', fields ['email']
        db.create_unique(u'core_member', ['email'])


    def backwards(self, orm):
        # Removing unique constraint on 'Member', fields ['email']
        db.delete_unique(u'core_member', ['email'])

        # Deleting field 'Member.first_name'
        db.delete_column(u'core_member', 'first_name')

        # Deleting field 'Member.last_name'
        db.delete_column(u'core_member', 'last_name')


    models = {
        'core.app': {
            'Meta': {'object_name': 'App'},
            'app_secret': ('django.db.models.fields.CharField', [], {'default': "'969a2477-1ea7-4fbb-af13-b5e39efee2ec'", 'max_length': '60'}),
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
            'api_key': ('django.db.models.fields.CharField', [], {'default': "'fe7d9676-0ac0-47bc-a42b-fa707b86ce73'", 'max_length': '60'}),
            'api_secret': ('django.db.models.fields.CharField', [], {'default': "'f493e05c-af8b-46d0-9407-90f10d52f786'", 'max_length': '60'}),
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