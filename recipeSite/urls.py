from django.urls import path
from recipeSite import views

app_name = 'recipeSite'

urlpatterns = [
   path('', views.index, name= 'index'),
   path('myAccount/', views.myAccount, name= 'myAccount'),
   path('savedRecipes/', views.savedRecipes, name= 'savedRecipes'),
   path('myRecipes/', views.myRecipes, name= 'myRecipes'),
   path('addRecipe/', views.addRecipe, name= 'addRecipe'),
   path('signout/', views.signOut, name= 'signout'),

]