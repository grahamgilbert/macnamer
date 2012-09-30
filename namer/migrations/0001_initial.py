# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ComputerGroup'
        db.create_table('namer_computergroup', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('namer', ['ComputerGroup'])

        # Adding model 'Prefix'
        db.create_table('namer_prefix', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('prefix', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('computer_group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['namer.ComputerGroup'])),
        ))
        db.send_create_signal('namer', ['Prefix'])

        # Adding model 'Computer'
        db.create_table('namer_computer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('prefix', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['namer.Prefix'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('namer', ['Computer'])


    def backwards(self, orm):
        # Deleting model 'ComputerGroup'
        db.delete_table('namer_computergroup')

        # Deleting model 'Prefix'
        db.delete_table('namer_prefix')

        # Deleting model 'Computer'
        db.delete_table('namer_computer')


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
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'prefix': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['namer']