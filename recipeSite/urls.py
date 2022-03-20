from xml.etree.ElementInclude import include
from django.urls import path
from recipeSite import views
from haystack.views import SearchView

app_name = 'recipeSite'

urlpatterns = [
   path('myRecipes/', views.myRecipes, name= 'myRecipes'),
   path('browse/', views.browseRecipe, name= 'browseRecipes'),
   path('savedRecipes/', views.savedRecipes, name= 'savedRecipes'),
   path('addRecipe/', views.AddRecipe.as_view(), name= 'addRecipe'),
   path('addComment/', views.AddComment.as_view(), name= 'addComment'),
   path('search/', SearchView(), name='haystack_search'),
   path('bookmark/', views.BookmarkRecipeView.as_view(), name='bookmark'),
   path('delete/', views.DeleteRecipeButton.as_view(), name='delete'),
   path('like/', views.LikeCategoryView.as_view(), name='like'),
   path('viewRecipe/<slug:recipe_name_slug>/',views.viewRecipe.as_view(), name='viewRecipe'),
   path('editRecipe/<slug:recipe_name_slug>/',views.editRecipe.as_view(), name='editRecipe'),
   #path('viewRecipe/', views.viewRecipe, name= 'viewRecipe'),
   #path('restricted/', views.restricted, name= 'restricted'),
]
