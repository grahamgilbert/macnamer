# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Prefix'
        db.delete_table('namer_prefix')

        # Adding field 'ComputerGroup.prefix'
        db.add_column('namer_computergroup', 'prefix',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ComputerGroup.domain'
        db.add_column('namer_computergroup', 'domain',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Computer.prefix'
        db.delete_column('namer_computer', 'prefix_id')

        # Adding field 'Computer.computergroup'
        db.add_column('namer_computer', 'computergroup',
                      self.gf('django.db.models.fields.related.ForeignKey'), to=orm['namer.ComputerGroup']),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'Prefix'
        db.create_table('namer_prefix', (
            ('computer_group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['namer.ComputerGroup'])),
            ('domain', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('prefix', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal('namer', ['Prefix'])

        # Deleting field 'ComputerGroup.prefix'
        db.delete_column('namer_computergroup', 'prefix')

        # Deleting field 'ComputerGroup.domain'
        db.delete_column('namer_computergroup', 'domain')

        # Adding field 'Computer.prefix'
        db.add_column('namer_computer', 'prefix',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['namer.Prefix']),
                      keep_default=False)

        # Deleting field 'Computer.computergroup'
        db.delete_column('namer_computer', 'computergroup_id')


    models = {
        'namer.computer': {
            'Meta': {'object_name': 'Computer'},
            'computergroup': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['namer.ComputerGroup']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
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
