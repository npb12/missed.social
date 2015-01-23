# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'OldUserProfile'
        db.delete_table(u'users_olduserprofile')

        # Adding field 'UserProfile.fName'
        db.add_column(u'users_userprofile', 'fName',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50, blank=True),
                      keep_default=False)

        # Adding field 'UserProfile.userType'
        db.add_column(u'users_userprofile', 'userType',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['users.UserType'], null=True),
                      keep_default=False)

        # Adding field 'UserProfile.interestedIn'
        db.add_column(u'users_userprofile', 'interestedIn',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['users.InterestType'], null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'OldUserProfile'
        db.create_table(u'users_olduserprofile', (
            ('interestedIn', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['users.InterestType'], null=True)),
            ('lName', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('userType', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['users.UserType'], null=True)),
            ('fName', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'users', ['OldUserProfile'])

        # Deleting field 'UserProfile.fName'
        db.delete_column(u'users_userprofile', 'fName')

        # Deleting field 'UserProfile.userType'
        db.delete_column(u'users_userprofile', 'userType_id')

        # Deleting field 'UserProfile.interestedIn'
        db.delete_column(u'users_userprofile', 'interestedIn_id')


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
            'timeStamp': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2015, 1, 23, 0, 0)'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['users.UserProfile']"})
        },
        u'users.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '255'}),
            'fName': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interestedIn': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['users.InterestType']", 'null': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_admin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'userType': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['users.UserType']", 'null': 'True'})
        },
        u'users.usertype': {
            'Meta': {'object_name': 'UserType'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['users']