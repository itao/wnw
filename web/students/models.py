from django.db import models

from accounts.models import User
from klasses.models import Klass
from schools.models import School

class Student(models.Model):
    account = models.ForeignKey(User)
    picture = models.ImageField(null=True, blank=True, upload_to="attachments/students/pictures/")
    klasses = models.ManyToManyField(Klass, blank=True, null=True)

    def name(self):
        return self.account.get_full_name()
