# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Location.user'
        db.alter_column(u'users_location', 'user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['users.UserProfile']))

    def backwards(self, orm):

        # Changing field 'Location.user'
        db.alter_column(u'users_location', 'user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['users.OldUserProfile']))

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
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['users.UserProfile']"})
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