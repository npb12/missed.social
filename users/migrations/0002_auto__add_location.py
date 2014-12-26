# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
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
        # Deleting model 'Location'
        db.delete_table(u'users_location')


    models = {
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
            'lName': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'})
        }
    }

    complete_apps = ['users']