# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Student'
        db.create_table(u'students_student', (
            (u'user_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['accounts.User'], unique=True, primary_key=True)),
            ('picture', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'students', ['Student'])

        # Adding M2M table for field klasses on 'Student'
        m2m_table_name = db.shorten_name(u'students_student_klasses')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('student', models.ForeignKey(orm[u'students.student'], null=False)),
            ('klass', models.ForeignKey(orm[u'klasses.klass'], null=False))
        ))
        db.create_unique(m2m_table_name, ['student_id', 'klass_id'])


    def backwards(self, orm):
        # Deleting model 'Student'
        db.delete_table(u'students_student')

        # Removing M2M table for field klasses on 'Student'
        db.delete_table(db.shorten_name(u'students_student_klasses'))


    models = {
        u'accounts.user': {
            'Meta': {'object_name': 'User'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '255'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"})
        },
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
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'klasses.klass': {
            'Meta': {'object_name': 'Klass'},
            'code': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '40', 'blank': 'True'}),
            'colour': ('django.db.models.fields.CharField', [], {'default': "'#999999'", 'max_length': '7'}),
            'coteachers': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'coclasses'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['teachers.Teacher']"}),
            'end': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'start': ('django.db.models.fields.DateField', [], {}),
            'teacher': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'classes'", 'to': u"orm['teachers.Teacher']"})
        },
        u'schools.school': {
            'Meta': {'object_name': 'School'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'students.student': {
            'Meta': {'object_name': 'Student', '_ormbases': [u'accounts.User']},
            'klasses': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'students'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['klasses.Klass']"}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'user_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['accounts.User']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'teachers.teacher': {
            'Meta': {'object_name': 'Teacher', '_ormbases': [u'accounts.User']},
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'school': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['schools.School']", 'null': 'True', 'blank': 'True'}),
            u'user_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['accounts.User']", 'unique': 'True', 'primary_key': 'True'})
        }
    }

    complete_apps = ['students']