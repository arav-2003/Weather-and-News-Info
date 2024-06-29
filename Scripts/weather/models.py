from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    name= models.CharField(max_length=255,default="NULL")
    dob = models.DateField()
    phone_number = models.CharField(max_length=255)
    email = models.CharField(max_length=255,default="NULL")
    password=models.CharField(max_length=255)

