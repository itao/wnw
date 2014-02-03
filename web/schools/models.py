from django.db import models

class School(models.Model):
    name = models.CharField(max_length=200)
    logo = models.ImageField(null=True, blank=True, upload_to="schools/pictures")
