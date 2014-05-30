# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'ComputerGroup.key'
        db.add_column(u'namer_computergroup', 'key',
                      self.gf('django.db.models.fields.CharField')(max_length=255, unique=True, null=True, blank=True),
                      keep_default=False)

        # Adding unique constraint on 'Network', fields ['network']
        db.create_unique(u'namer_network', ['network'])


    def backwards(self, orm):
        # Removing unique constraint on 'Network', fields ['network']
        db.delete_unique(u'namer_network', ['network'])

        # Deleting field 'ComputerGroup.key'
        db.delete_column(u'namer_computergroup', 'key')


    models = {
        u'namer.computer': {
            'Meta': {'ordering': "['name']", 'object_name': 'Computer'},
            'computergroup': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['namer.ComputerGroup']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_checkin': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'serial': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'})
        },
        u'namer.computergroup': {
            'Meta': {'object_name': 'ComputerGroup'},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'prefix': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'namer.network': {
            'Meta': {'ordering': "['network']", 'object_name': 'Network'},
            'computergroup': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['namer.ComputerGroup']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'network': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'})
        }
    }

    complete_apps = ['namer']