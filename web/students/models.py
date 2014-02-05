from django.db import models

from accounts.models import User
from klasses.models import Klass

class Student(models.Model):
    account = models.ForeignKey(User, default=None, null=True, blank=True)
    picture = models.ImageField(null=True, blank=True, upload_to="students/pictures")
    klasses = models.ManyToManyField(Klass, blank=True, null=True, related_name="students")

    def name(self):
        if self.account is not None:
            return self.account.get_full_name()
        else:
            return ''


# Assume comma-separated values: first name, last name, email (optional, ID (optional)
def parse_new_student_list(data):
    data = data.split('\r\n')

    student_list = []
    for row in data:
        row = row.split(',').strip()
        first_name = r[0]
        last_name = r[1]
        email = r[2]
        student_id = r[3]

    return student_list
