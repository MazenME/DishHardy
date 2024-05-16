# models.py

from django.db import models


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    instructions = models.CharField(max_length=50000)
    image = models.URLField( max_length=200000)
    is_favoured = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.name}"


class Ingredient(models.Model):
    recipe_id = models.ForeignKey(
        'recipeFinder.Recipe',
        related_name='ingredients',
        on_delete=models.CASCADE,
        to_field='id'
    )
    name = models.CharField(max_length=100)
    quantity = models.FloatField()
    unit = models.CharField(max_length=10)
    
    def __str__(self):
        return f"{self.name}"
