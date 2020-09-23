from django.db import models

from .specialty import Specialty

class Vet(models.Model):
    first_name = models.CharField(max_length = 128)
    last_name = models.CharField(max_length = 128)
    specialties = models.ManyToManyField(Specialty)
    
    def __str__(self):
        return self.first_name + " " + self.last_name