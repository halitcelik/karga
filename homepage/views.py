# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponseRedirect
from django.shortcuts import render
from models import Recipe, HopType
from forms import RecipeForm, HopTypeForm

# Create your views here.


def home(request):
    recipes = Recipe.objects.all()
    return render(request, 'home.html', {'recipes': recipes})


def add_recipe(request):
    if request.method == 'POST':
        recipe_form = RecipeForm(request.POST, request.FILES)
        hop_type_form = HopTypeForm(request.POST)
        hop_counter = request.POST.get('hop-counter')
        hop_counter = int(hop_counter) + 1

        if recipe_form.is_valid():
            recipe = recipe_form.save()

            for i in range(hop_counter):
                if i == 0:
                    hop_type_dict = {'hop_type': request.POST.get('hop_type')}
                else:
                    hop_type_dict = {'hop_type': request.POST.get('hop_type_%d' % i)}

                hop_type_form = HopTypeForm(hop_type_dict)
                if hop_type_form.is_valid():
                    hop = hop_type_form.save(commit=False)
                    hop.recipe = recipe
                    hop.save()

            return HttpResponseRedirect('/thanks/')
    else:
        recipe_form = RecipeForm()
        hop_type_form = HopTypeForm()
    return render(request, 'add-recipe.html', {'hop_type_form': hop_type_form, 'recipe_form': recipe_form})


def thanks(request):
    return render(request, 'thanks.html')
