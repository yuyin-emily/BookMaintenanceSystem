from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Student(AbstractUser):
    studentId = models.CharField(max_length=10,null=True)
    reister_year = models.IntegerField(null=True)
    phone_number = models.CharField(max_length=10,blank=True,null=True)
    gender = models.CharField(max_length=1,choices = (("M","Male"),("F","Female")),null=True)
    birth_date = models.DateField(null=True)
    