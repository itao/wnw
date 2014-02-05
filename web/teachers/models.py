from django.db import models

from accounts.models import User
from schools.models import School
# from klasses.models import Klass
from notes.models import Note

class Teacher(models.Model):
    account = models.ForeignKey(User)
    picture = models.ImageField(null=True, blank=True, upload_to="teachers/pictures")
    school = models.ForeignKey(School, null=True, blank=True)
    # klasses = models.ManyToManyField(Klass, blank=True, null=True)
    notes = models.ForeignKey(Note, blank=True, null=True)

    def name(self):
        return self.account.get_full_name()
