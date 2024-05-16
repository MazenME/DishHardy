from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from recipeFinder.models import Recipe, Ingredient
from django.contrib.auth.decorators import login_required



#view all recipes
@login_required(login_url='login')
def view_recipes(request):
    recipes = Recipe.objects.all()
    return render(request, 'all_recipes.html', {'recipes': recipes})
#end view


# search
@login_required(login_url='login')
def search(request):
    recipe_query = request.GET.get('name')
    ingredient_query = request.GET.get('ingredient')
    recipes = []

    if recipe_query:
        recipes_by_name = Recipe.objects.filter(name__icontains=recipe_query)
        recipes.extend(recipes_by_name)

    elif ingredient_query:
        ingredients = Ingredient.objects.filter(name__icontains=ingredient_query)
        recipes_by_ingredient = Recipe.objects.filter(ingredients__in=ingredients)
        recipes.extend(recipes_by_ingredient)

    return render(request, 'search.html', {
        'recipe_query': recipe_query,
        'ingredient_query': ingredient_query,
        'recipes': recipes
    })
#end search




#add to favourite
@login_required(login_url='login')
def add_to_favorites(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    recipe.is_favoured = True
    recipe.save()
    return redirect(request.META.get('HTTP_REFERER'))
#end add to favourite



@login_required(login_url='login')
def favourite_recipes(request):
    # Retrieve all recipes that are favoured
    favoured_recipes = Recipe.objects.filter(is_favoured=True)
    return render(request, 'Favourite.html', {'favoured_recipes': favoured_recipes})

@login_required(login_url='login')
def remove_favourite(request):
    if request.method == 'POST':
        recipe_id = request.POST.get('recipe_id')
        recipe = Recipe.objects.get(id=recipe_id)
        recipe.is_favoured = False
        recipe.save()
        return redirect('favourite_recipes')

@login_required(login_url='login')
def recipe_details_view(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)

    context = {
        'recipe': recipe,
    }
    return render(request, 'details.html', context)


# add recipe
@login_required(login_url='login')
def add_form(request):
    if request.method == 'POST':
        recipe_name = request.POST.get('recipe-name')
        course = request.POST.get('course')
        recipe_image = request.POST.get('recipe-image')
        recipe_description = request.POST.get('recipe-description')
    
        recipe = Recipe.objects.create(
            name=recipe_name,
            course=course,
            instructions=recipe_description,
            image=recipe_image
        )
        ingredient_names = request.POST.getlist('ingredient-name[]')
        ingredient_quantities = request.POST.getlist('ingredient-quantity[]')
        ingredient_units = request.POST.getlist('ingredient-unit[]')
        
        for name, quantity, unit in zip(ingredient_names, ingredient_quantities, ingredient_units):
            ingredient = Ingredient.objects.create(
                recipe_id = recipe,
                name = name,
                quantity = quantity,
                unit = unit
            )
        return render(request, 'add-form.html')
    else:
        return render(request, 'add-form.html')
    


def home(request):
    return render(request,'home.html')
        

@login_required(login_url='login')
def show_recipes(request):
    recipes = Recipe.objects.all()
    return render(request, 'delete-and-update.html', {'recipes': recipes})

#delete
@login_required(login_url='login')
def delete_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    recipe.delete()
    return redirect('show_manage')

#update form
@login_required(login_url='login')
def update_form(request, recipe_id):
    if request.method == 'POST':
        recipe = get_object_or_404(Recipe, pk=recipe_id) 
        ingredients = Ingredient.objects.filter(recipe_id=recipe)
        return render(request, 'update-form.html', {'recipe': recipe, 'ingredients': ingredients})
    
#edit
@login_required(login_url='login')
def edit_recipe(request, recipe_id):
    if request.method == 'POST':
        recipe = get_object_or_404(Recipe, pk=recipe_id) 
        ingredients = Ingredient.objects.filter(recipe_id=recipe)

        recipe.name = request.POST.get('recipe-name')
        recipe.course = request.POST.get('course')
        recipe.image = request.POST.get('recipe-image')
        recipe.instructions = request.POST.get('recipe-description')
        recipe.save()

        ingredient_names = request.POST.getlist('ingredient-name[]')
        ingredient_quantities = request.POST.getlist('ingredient-quantity[]')
        ingredient_units = request.POST.getlist('ingredient-unit[]')
        recipe.ingredients.all().delete()

        for name, quantity, unit in zip(ingredient_names, ingredient_quantities, ingredient_units):
            ingredient = Ingredient.objects.create(
                recipe_id = recipe,
                name = name,
                quantity = quantity,
                unit = unit
            )
        return redirect('show_manage')
    else:
        return render(request, 'delete-and-update.html')



def ho (request):
    return render(request,'ho.html')