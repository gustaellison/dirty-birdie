from django.db import models
from django.urls import reverse
from datetime import date

# Create your models here.
MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

class NestingMaterial(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=51)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('nestingmaterials_detail', kwargs={'pk': self.id})


class Bird(models.Model):
    species = models.CharField(max_length=100)
    habitat = models.CharField(max_length=100)
    location = models.CharField(max_length=300) 
    image = models.CharField(max_length=100)
    description = models.CharField(max_length=500, default="No description added yet")
    nestingmaterials = models.ManyToManyField(NestingMaterial)

    def __str__(self):
        return f'{self.species} ({self.id})'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'bird_id': self.id})
    
    def fed_for_today(self):
        return self.feeding_set.filter(date=date.today()).count() >= len(MEALS)

class Feeding(models.Model):
    date = models.DateField('Feeding Date')
    meal = models.CharField(
        max_length=1,
        choices = MEALS,
        default=MEALS[0][0]
        )
    bird = models.ForeignKey(Bird, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.get_meal_display()} on {self.date}"
    
    class Meta:
        ordering = ['-date']


