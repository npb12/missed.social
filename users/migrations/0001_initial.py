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

        # Adding model 'UserProfile'
        db.create_table(u'users_userprofile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('last_login', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('email', self.gf('django.db.models.fields.EmailField')(unique=True, max_length=255)),
        ))
        db.send_create_signal(u'users', ['UserProfile'])

        # Adding model 'OldUserProfile'
        db.create_table(u'users_olduserprofile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fName', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('lName', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('userType', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['users.UserType'], null=True)),
            ('interestedIn', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['users.InterestType'], null=True)),
        ))
        db.send_create_signal(u'users', ['OldUserProfile'])

        # Adding model 'Location'
        db.create_table(u'users_location', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['users.OldUserProfile'])),
            ('latitude', self.gf('django.db.models.fields.DecimalField')(default=1, max_digits=12, decimal_places=8)),
            ('longitude', self.gf('django.db.models.fields.DecimalField')(default=1, max_digits=12, decimal_places=8)),
            ('timeStamp', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2015, 1, 22, 0, 0))),
        ))
        db.send_create_signal(u'users', ['Location'])


    def backwards(self, orm):
        # Deleting model 'InterestType'
        db.delete_table(u'users_interesttype')

        # Deleting model 'UserType'
        db.delete_table(u'users_usertype')

        # Deleting model 'UserProfile'
        db.delete_table(u'users_userprofile')

        # Deleting model 'OldUserProfile'
        db.delete_table(u'users_olduserprofile')

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
            'latitude': ('django.db.models.fields.DecimalField', [], {'default': '1', 'max_digits': '12', 'decimal_places': '8'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'default': '1', 'max_digits': '12', 'decimal_places': '8'}),
            'timeStamp': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2015, 1, 22, 0, 0)'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['users.OldUserProfile']"})
        },
        u'users.olduserprofile': {
            'Meta': {'object_name': 'OldUserProfile'},
            'fName': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interestedIn': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['users.InterestType']", 'null': 'True'}),
            'lName': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'userType': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['users.UserType']", 'null': 'True'})
        },
        u'users.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'users.usertype': {
            'Meta': {'object_name': 'UserType'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['users']