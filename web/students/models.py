from django.db import models

from accounts.models import User
from klasses.models import Klass

class Student(models.Model):
    account = models.ForeignKey(User, default=None, null=True, blank=True)
    picture = models.ImageField(null=True, blank=True, upload_to="students/pictures")
    klasses = models.ManyToManyField(Klass, blank=True, null=True, related_name="students")

    def name(self):
        return self.account.get_full_name()