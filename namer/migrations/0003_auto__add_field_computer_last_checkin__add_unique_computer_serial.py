# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Computer.last_checkin'
        db.add_column('namer_computer', 'last_checkin',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 10, 10, 0, 0)),
                      keep_default=False)

        # Adding unique constraint on 'Computer', fields ['serial']
        db.create_unique('namer_computer', ['serial'])


    def backwards(self, orm):
        # Removing unique constraint on 'Computer', fields ['serial']
        db.delete_unique('namer_computer', ['serial'])

        # Deleting field 'Computer.last_checkin'
        db.delete_column('namer_computer', 'last_checkin')


    models = {
        'namer.computer': {
            'Meta': {'object_name': 'Computer'},
            'computergroup': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['namer.ComputerGroup']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_checkin': ('django.db.models.fields.DateTimeField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'serial': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'})
        },
        'namer.computergroup': {
            'Meta': {'object_name': 'ComputerGroup'},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'prefix': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['namer']