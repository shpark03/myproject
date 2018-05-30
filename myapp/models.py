from django.db import models

# Create your models here.

class Dreamreal(models.Model):

   website = models.CharField(max_length = 50)
   mail = models.CharField(max_length = 50)
   name = models.CharField(max_length = 50)
   phonenumber = models.IntegerField()
   online = models.ForeignKey('Online', on_delete=models.CASCADE, default = 1)

   class Meta:
      db_table = "dreamreal"

class Online(models.Model):
   domain = models.CharField(max_length = 30)
   
   class Meta:
      db_table = "online"
