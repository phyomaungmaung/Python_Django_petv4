from django.db import models

# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    contact = models.IntegerField(default=0)
    email = models.EmailField(max_length=50,default='test@gmail.com')
    age = models.IntegerField(default=0)