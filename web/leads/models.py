from django.db import models

# Create your models here.
class Lead(models.Model):
   name = models.CharField(max_length=200)
   school_type = models.CharField(max_length=200)
   grades = models.CharField(max_length=200)
   tuition = models.CharField(max_length=200)
   size = models.CharField(max_length=200)
   enrollment = models.CharField(max_length=200)
   phone = models.CharField(max_length=200)
   street = models.CharField(max_length=200)
   city = models.CharField(max_length=200)
   region = models.CharField(max_length=200)
   postal = models.CharField(max_length=200)
