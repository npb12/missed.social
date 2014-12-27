# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'InterestType'
        db.create_table(u'users_interesttype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'users', ['InterestType'])

        # Adding model 'UserType'
        db.create_table(u'users_usertype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'users', ['UserType'])

        # Adding model 'User'
        db.create_table(u'users_user', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fName', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('lName', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('userType', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['users.UserType'], null=True)),
            ('interestedIn', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['users.InterestType'], null=True)),
        ))
        db.send_create_signal(u'users', ['User'])

        # Adding model 'Location'
        db.create_table(u'users_location', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['users.User'])),
            ('latitude', self.gf('django.db.models.fields.DecimalField')(default=1, max_digits=10, decimal_places=5)),
            ('longitude', self.gf('django.db.models.fields.DecimalField')(default=1, max_digits=10, decimal_places=5)),
            ('timeStamp', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 12, 26, 0, 0))),
        ))
        db.send_create_signal(u'users', ['Location'])


    def backwards(self, orm):
        # Deleting model 'InterestType'
        db.delete_table(u'users_interesttype')

        # Deleting model 'UserType'
        db.delete_table(u'users_usertype')

        # Deleting model 'User'
        db.delete_table(u'users_user')

        # Deleting model 'Location'
        db.delete_table(u'users_location')


    models = {
        u'users.interesttype': {
            'Meta': {'object_name': 'InterestType'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'users.location': {
            'Meta': {'object_name': 'Location'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'default': '1', 'max_digits': '10', 'decimal_places': '5'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'default': '1', 'max_digits': '10', 'decimal_places': '5'}),
            'timeStamp': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 12, 26, 0, 0)'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['users.User']"})
        },
        u'users.user': {
            'Meta': {'object_name': 'User'},
            'fName': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interestedIn': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['users.InterestType']", 'null': 'True'}),
            'lName': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'userType': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['users.UserType']", 'null': 'True'})
        },
        u'users.usertype': {
            'Meta': {'object_name': 'UserType'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['users']