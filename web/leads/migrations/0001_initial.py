# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Lead'
        db.create_table(u'leads_lead', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('school_type', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('grades', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('tuition', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('size', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('enrollment', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('street', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('region', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('postal', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('last_contact', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('comments', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'leads', ['Lead'])


    def backwards(self, orm):
        # Deleting model 'Lead'
        db.delete_table(u'leads_lead')


    models = {
        u'leads.lead': {
            'Meta': {'object_name': 'Lead'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'comments': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'enrollment': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'grades': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_contact': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'postal': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'school_type': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'size': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'tuition': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['leads']