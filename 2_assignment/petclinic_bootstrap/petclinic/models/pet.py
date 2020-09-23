from django.db import models

from .owner import Owner
from .pet_type import PetType

class Pet(models.Model):
    name = models.CharField(max_length=30)
    owner_id = models.ForeignKey(Owner,on_delete=models.CASCADE)
    pet_type_id = models.ForeignKey(PetType, name='pettype', on_delete=models.CASCADE)
    birthday = models.DateTimeField(name='birthday',default=None)

    def __str__(self):
        return self.name