# empapp/models.py
from django.db import models

class Employee(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    age = models.IntegerField()
    address = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.fname} {self.lname}"



