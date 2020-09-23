from django.db import models

# Create your models here.
class PetType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Food(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    calories = models.FloatField(default=0.0)
    amount = models.FloatField(default=0.0)

    def __str__(self):
        return self.name

class Pet(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    pet_type_id = models.ForeignKey(PetType, name='pettype', on_delete=models.CASCADE)
    food_id = models.ForeignKey(Food, name='food', on_delete=models.CASCADE)
    hungry = models.BooleanField(default=False)
    weight = models.FloatField(default=0.0)
    birthday = models.DateTimeField(name='birthday',default=None)
    age = models.IntegerField(default=0)
    photo = models.ImageField()

    def __str__(self):
        return self.name

class Specialty(models.Model):
    name = models.CharField(max_length = 128)
    
    def __str__(self):
        return self.name

class Vet(models.Model):
    first_name = models.CharField(max_length = 128)
    last_name = models.CharField(max_length = 128)
    specialties = models.ManyToManyField(Specialty)
    
    def __str__(self):
        return self.first_name + " " + self.last_name

class Visit(models.Model):
    visit_date = models.DateTimeField()
    description = models.TextField()
    pet = models.ForeignKey(Pet,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.description

class Owner(models.Model):
    first_name = models.CharField(max_length = 128)
    last_name = models.CharField(max_length = 128)
    address = models.CharField(max_length = 256)
    city = models.CharField(max_length = 128)
    telephone = models.CharField(max_length = 20)
    
    def __str__(self):
        return self.first_name + " " + self.last_name 