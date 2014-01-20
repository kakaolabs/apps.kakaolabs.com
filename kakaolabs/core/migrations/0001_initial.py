# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Member'
        db.create_table(u'core_member', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('last_login', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=200, unique=True, null=True, db_index=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=254, null=True, db_index=True)),
            ('is_admin', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('date_joined', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_index=True, blank=True)),
            ('api_key', self.gf('django.db.models.fields.CharField')(default='00e44c35-cca2-492a-aad8-06006d50db26', max_length=60)),
            ('api_secret', self.gf('django.db.models.fields.CharField')(default='115a8f65-6a6a-4ded-a1ce-323831f4c089', max_length=60)),
        ))
        db.send_create_signal('core', ['Member'])

        # Adding model 'App'
        db.create_table(u'core_app', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('member', self.gf('django.db.models.fields.related.ForeignKey')(related_name='apps', to=orm['core.Member'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('image_url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True)),
            ('app_secret', self.gf('django.db.models.fields.CharField')(default='e323ada2-4c90-4cc7-b2e8-8b2ed845bdc4', max_length=60)),
        ))
        db.send_create_signal('core', ['App'])

        # Adding M2M table for field devices on 'App'
        m2m_table_name = db.shorten_name(u'core_app_devices')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('app', models.ForeignKey(orm['core.app'], null=False)),
            ('device', models.ForeignKey(orm['core.device'], null=False))
        ))
        db.create_unique(m2m_table_name, ['app_id', 'device_id'])

        # Adding model 'AppVersion'
        db.create_table(u'core_appversion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('app', self.gf('django.db.models.fields.related.ForeignKey')(related_name='apps', to=orm['core.App'])),
            ('os', self.gf('django.db.models.fields.SmallIntegerField')(default=0, db_index=True)),
            ('version', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('subversion', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('download_url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal('core', ['AppVersion'])

        # Adding model 'Device'
        db.create_table(u'core_device', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('token', self.gf('django.db.models.fields.CharField')(max_length=200, unique=True, null=True, db_index=True)),
            ('os', self.gf('django.db.models.fields.SmallIntegerField')(default=0, db_index=True)),
            ('device_type', self.gf('django.db.models.fields.CharField')(max_length=100, db_index=True)),
            ('os_version', self.gf('django.db.models.fields.CharField')(max_length=20, db_index=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_index=True, blank=True)),
        ))
        db.send_create_signal('core', ['Device'])


    def backwards(self, orm):
        # Deleting model 'Member'
        db.delete_table(u'core_member')

        # Deleting model 'App'
        db.delete_table(u'core_app')

        # Removing M2M table for field devices on 'App'
        db.delete_table(db.shorten_name(u'core_app_devices'))

        # Deleting model 'AppVersion'
        db.delete_table(u'core_appversion')

        # Deleting model 'Device'
        db.delete_table(u'core_device')


    models = {
        'core.app': {
            'Meta': {'object_name': 'App'},
            'app_secret': ('django.db.models.fields.CharField', [], {'default': "'7dea7248-e9a9-43fc-a6e5-e2350e92e7a5'", 'max_length': '60'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'devices': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['core.Device']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
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
            'api_key': ('django.db.models.fields.CharField', [], {'default': "'a74c466e-1ebb-4b09-9804-f824226c8879'", 'max_length': '60'}),
            'api_secret': ('django.db.models.fields.CharField', [], {'default': "'92980f54-10d0-46ae-bd59-b8880023a768'", 'max_length': '60'}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '254', 'null': 'True', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_admin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '200', 'unique': 'True', 'null': 'True', 'db_index': 'True'})
        }
    }

    complete_apps = ['core']