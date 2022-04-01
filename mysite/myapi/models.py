# models.py
from django.db import models

class Hero(models.Model):
    name = models.CharField(max_length=60)
    alias = models.CharField(max_length=60)
    
    def __str__(self):
        return self.name
        

class StudentDetail(models.Model):
    firstname = models.CharField(max_length=60)
    lastname = models.CharField(max_length=60)
    grade = models.PositiveIntegerField()
    mailid = models.CharField(max_length=200)
    contactnumber = models.CharField(max_length=60)
    adharnumber = models.CharField(max_length=60)
    address = models.CharField(max_length=200)
    vaccinationstatus = models.CharField(max_length=60)
    
    def __str__(self):
        return "%s, %s" % (self.lastname, self.firstname)