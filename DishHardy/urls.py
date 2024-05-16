"""
URL configuration for DishHardy project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
"""
URL configuration for DishHardy project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from recipeFinder.views import favourite_recipes, remove_favourite, recipe_details_view, search, add_to_favorites,view_recipes
from recipeFinder.views import home
from django.urls import path
from recipeFinder.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('favourite/', favourite_recipes, name='favourite_recipes'),
    path('remove-favourite/', remove_favourite, name='remove_favourite'),
    path('search/', search, name='search'),
    path('view_recipes/', view_recipes, name='view_recipes'),
    path('recipe-details/<int:recipe_id>/', recipe_details_view, name='recipe_details'),
    path('add_to_favorites/<int:recipe_id>/',add_to_favorites, name='add_to_favorites'),


    path('register', include('registeration.reUrls')),
    path('',ho,name='home'),

    
    path('addform/', add_form, name='add_form'),
    path('manage-recipes/', show_recipes, name='show_manage'),
    path('manage-recipes/<int:recipe_id>/delete', delete_recipe, name='delete_recipe'),
    path('updateform/<int:recipe_id>', update_form, name='update_form'),
    path('edit-recipes/<int:recipe_id>', edit_recipe, name='edit_recipe'),

]

