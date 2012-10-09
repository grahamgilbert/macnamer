# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Prefix.domain'
        db.add_column('namer_prefix', 'domain',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Prefix.domain'
        db.delete_column('namer_prefix', 'domain')


    models = {
        'namer.computer': {
            'Meta': {'object_name': 'Computer'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'prefix': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['namer.Prefix']"})
        },
        'namer.computergroup': {
            'Meta': {'object_name': 'ComputerGroup'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'namer.prefix': {
            'Meta': {'object_name': 'Prefix'},
            'computer_group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['namer.ComputerGroup']"}),
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'prefix': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['namer']