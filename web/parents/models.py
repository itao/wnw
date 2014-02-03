from django.db import models

from accounts.models import User
from students.models import Student

class Parent(models.Model):
    account = models.ForeignKey(User)
    picture = models.ImageField(null=True, blank=True, upload_to="parents/pictures")
    children = models.ManyToManyField(Student, blank=True, null=True)

    def name(self):
        return self.account.get_full_name()
