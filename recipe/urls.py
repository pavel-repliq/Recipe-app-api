"""
   urls mapping for recipe app 
"""
from django.urls import path
from recipe.views import *

app_name = "recipe"
urlpatterns = [
   path("recipe_list/", RecipeCreateAndListView.as_view(), name="recipe_list"),

]