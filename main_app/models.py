from django.db import models

# Create your models here.

class Bird(models.Model):
    species = models.CharField(max_length=100)
    habitat = models.CharField(max_length=100)
    location = models.CharField(max_length=300) 
    image = models.CharField(max_length=100)
    description = models.CharField(max_length=500, default="No description added yet")

    def __str__(self):
        return self.species

