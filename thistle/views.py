from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Ingredient
from .models import Recipe
from django.http import JsonResponse
from django.core import serializers
from django.template import RequestContext


def index(request):
    template = loader.get_template('thistle/index.html')

    recipes = Recipe.objects.all()
    all_ingredients = Ingredient.objects.all()

    context = {"recipes": recipes, "all_ingredients": all_ingredients}
    return HttpResponse(template.render(context, request))


def save_recipe_changes(request):
    posted_ingredients = request.POST['ingredients'].split(", ")
    recipe_id = request.POST['recipeId']
    recipe = Recipe.objects.get(id=recipe_id)
    existing_ingredients = list(Ingredient.objects.filter(
        recipe=recipe).values_list('name', flat=True))
    
    for i in posted_ingredients:
        if i not in existing_ingredients:
            new_ingredient = Ingredient.objects.get_or_create(
                name = i
            )[0]
            print(new_ingredient)
            print(recipe.ingredients)
            recipe.ingredients.add(new_ingredient)
    
    for i in existing_ingredients:
        if i not in posted_ingredients and Ingredient.objects.filter(name=i).exists():
            recipe.ingredients.remove(Ingredient.objects.get(name=i))

    recipe.save()

    return HttpResponse()
