from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=200)

class Recipe(models.Model):
    name = models.CharField(max_length=200)
    ingredients = models.ManyToManyField(Ingredient)
