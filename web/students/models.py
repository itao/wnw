from django.db import models

from accounts.models import User
from klasses.models import Klass

class Student(models.Model):
    account = models.ForeignKey(User)
    picture = models.ImageField(null=True, blank=True, upload_to="students/pictures")
    klasses = models.ManyToManyField(Klass, blank=True, null=True)

    def name(self):
        return self.account.get_full_name()
