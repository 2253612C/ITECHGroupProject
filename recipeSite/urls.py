from django.urls import path
from recipeSite import views

app_name = 'recipeSite'

urlpatterns = [
   path('savedRecipes/', views.savedRecipes, name= 'savedRecipes'),
   path('myRecipes/', views.myRecipes, name= 'myRecipes'),
   path('addRecipe/', views.addRecipe, name= 'addRecipe'),
   path('restricted/', views.restricted, name= 'restricted'),

]