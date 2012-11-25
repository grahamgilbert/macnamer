# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Network'
        db.create_table('namer_network', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('network', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('computergroup', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['namer.ComputerGroup'])),
        ))
        db.send_create_signal('namer', ['Network'])


    def backwards(self, orm):
        # Deleting model 'Network'
        db.delete_table('namer_network')


    models = {
        'namer.computer': {
            'Meta': {'ordering': "['name']", 'object_name': 'Computer'},
            'computergroup': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['namer.ComputerGroup']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_checkin': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'serial': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'})
        },
        'namer.computergroup': {
            'Meta': {'object_name': 'ComputerGroup'},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'prefix': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        'namer.network': {
            'Meta': {'ordering': "['network']", 'object_name': 'Network'},
            'computergroup': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['namer.ComputerGroup']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'network': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['namer']