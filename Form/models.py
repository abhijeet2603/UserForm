from django.db import models


# Create your models here.

class FormInfo(models.Model):
    Name = models.CharField(max_length=50)
    Dob = models.DateField()
    Email = models.EmailField()
    Mobile = models.CharField(max_length=10)


