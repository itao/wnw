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

def import_csv(file):
   f = open(file, 'rb')
   read = csv.reader(f)
   for row in read:
      a = Lead(name=row[0], school_type=row[1], grades=row[2], tuition=row[3], size=row[4], enrollment=row[5], phone=row[6], street=row[7], city=row[8], region=row[9], postal=row[10])
      a.save()