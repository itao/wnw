from django.db import models

from teachers.models import Teacher

class Klass(models.Model):
    teacher = models.ForeignKey(Teacher)
    title = models.CharField(max_length=200)
    code = models.CharField(max_length=40, default='')
    start = models.DateField(verbose_name='Start Date')
    end = models.DateField(verbose_name='End Date')
    colour = models.CharField(max_length=7, default='#999999')

    def name(self):
        return self.title

    def num_students(self):
        return self.student_set.count()
