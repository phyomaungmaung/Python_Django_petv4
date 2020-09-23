from django.db import models

class Owner(models.Model):
    first_name = models.CharField(max_length = 128)
    last_name = models.CharField(max_length = 128)
    address = models.CharField(max_length = 256)
    city = models.CharField(max_length = 128)
    telephone = models.CharField(max_length = 20)
    
    def __str__(self):
        return self.first_name + " " + self.last_name