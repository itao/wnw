from django.db import models

from accounts.models import User
from schools.models import School

class Teacher(models.Model):
    account = models.ForeignKey(User)
    picture = models.ImageField(null=True, blank=True, upload_to="attachments/teachers/pictures/")
    school = models.ForeignKey(School, null=True, blank=True)

    def name(self):
        return self.account.get_full_name()
