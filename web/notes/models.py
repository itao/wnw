from django.db import models

from klasses.models import Klass
from students.models import Student

class Note(models.Model):
    klass = models.ForeignKey(Klass)
    students = models.ManyToManyField(Student, blank=True, null=True)
    detail = models.TextField(blank=True)
