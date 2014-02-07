from django.db import models

from accounts.models import User
from schools.models import School

class Teacher(User):
    picture = models.ImageField(null=True, blank=True, upload_to="teachers/pictures")
    school = models.ForeignKey(School, null=True, blank=True)
