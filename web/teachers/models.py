from django.db import models

from accounts.models import User

class Teacher(models.Model):
    account = models.ForeignKey(User)
    picture = models.ImageField(null=True, blank=True, upload_to="attachments/teachers/pictures/")

    def name(self):
        return self.account.get_full_name()
