# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'LocalPost'
        db.create_table(u'comm_localpost', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['django_facebook.FacebookCustomUser'])),
            ('latitude', self.gf('django.db.models.fields.DecimalField')(default=1, max_digits=12, decimal_places=8)),
            ('longitude', self.gf('django.db.models.fields.DecimalField')(default=1, max_digits=12, decimal_places=8)),
            ('timeStamp', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2015, 2, 28, 0, 0))),
            ('msg', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'comm', ['LocalPost'])

        # Adding model 'msgToUser'
        db.create_table(u'comm_msgtouser', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fromUser', self.gf('django.db.models.fields.related.ForeignKey')(related_name='msg_fromUser', to=orm['django_facebook.FacebookCustomUser'])),
            ('toUser', self.gf('django.db.models.fields.related.ForeignKey')(related_name='msg_toUser', to=orm['django_facebook.FacebookCustomUser'])),
            ('timeStamp', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2015, 2, 28, 0, 0))),
            ('msg', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('isRead', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'comm', ['msgToUser'])

        # Adding model 'Wave'
        db.create_table(u'comm_wave', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fromUser', self.gf('django.db.models.fields.related.ForeignKey')(related_name='wave_fromUser', to=orm['django_facebook.FacebookCustomUser'])),
            ('toUser', self.gf('django.db.models.fields.related.ForeignKey')(related_name='wave_toUser', to=orm['django_facebook.FacebookCustomUser'])),
            ('timeStamp', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2015, 2, 28, 0, 0))),
            ('isAccepted', self.gf('django.db.models.fields.CharField')(default='U', max_length=2)),
            ('isSeen', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'comm', ['Wave'])


    def backwards(self, orm):
        # Deleting model 'LocalPost'
        db.delete_table(u'comm_localpost')

        # Deleting model 'msgToUser'
        db.delete_table(u'comm_msgtouser')

        # Deleting model 'Wave'
        db.delete_table(u'comm_wave')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'comm.localpost': {
            'Meta': {'object_name': 'LocalPost'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'default': '1', 'max_digits': '12', 'decimal_places': '8'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'default': '1', 'max_digits': '12', 'decimal_places': '8'}),
            'msg': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'timeStamp': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2015, 2, 28, 0, 0)'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['django_facebook.FacebookCustomUser']"})
        },
        u'comm.msgtouser': {
            'Meta': {'object_name': 'msgToUser'},
            'fromUser': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'msg_fromUser'", 'to': u"orm['django_facebook.FacebookCustomUser']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isRead': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'msg': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'timeStamp': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2015, 2, 28, 0, 0)'}),
            'toUser': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'msg_toUser'", 'to': u"orm['django_facebook.FacebookCustomUser']"})
        },
        u'comm.wave': {
            'Meta': {'object_name': 'Wave'},
            'fromUser': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'wave_fromUser'", 'to': u"orm['django_facebook.FacebookCustomUser']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isAccepted': ('django.db.models.fields.CharField', [], {'default': "'U'", 'max_length': '2'}),
            'isSeen': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'timeStamp': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2015, 2, 28, 0, 0)'}),
            'toUser': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'wave_toUser'", 'to': u"orm['django_facebook.FacebookCustomUser']"})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'django_facebook.facebookcustomuser': {
            'Meta': {'object_name': 'FacebookCustomUser'},
            'about_me': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'access_token': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'blog_url': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'date_of_birth': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'facebook_id': ('django.db.models.fields.BigIntegerField', [], {'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'facebook_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'facebook_open_graph': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'facebook_profile_url': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'new_token_required': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'raw_data': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'website_url': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['comm']