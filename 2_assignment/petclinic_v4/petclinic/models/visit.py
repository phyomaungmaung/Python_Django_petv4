from django.db import models

from .pet import Pet

class Visit(models.Model):
    visit_date = models.DateTimeField()
    description = models.TextField()
    pet = models.ForeignKey(Pet,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.description