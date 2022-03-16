from xml.etree.ElementInclude import include
from django.urls import path
from recipeSite import views
from haystack.views import SearchView

app_name = 'recipeSite'

urlpatterns = [
   path('savedRecipes/', views.savedRecipes, name= 'savedRecipes'),
   path('myRecipes/', views.myRecipes, name= 'myRecipes'),
   path('addRecipe/', views.addRecipe, name= 'addRecipe'),
   path('search/', SearchView(), name='haystack_search'),
   path('<slug:recipe_name_slug>/',views.viewRecipe.as_view(), name='viewRecipe'),
   #path('viewRecipe/', views.viewRecipe, name= 'viewRecipe'),
   #path('restricted/', views.restricted, name= 'restricted'),
]
