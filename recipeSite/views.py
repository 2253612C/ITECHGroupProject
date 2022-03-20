from django.shortcuts import render,redirect,reverse
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required
from recipeSite.forms import *
from django.http import JsonResponse
from django.views import View
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.urls import resolve
from django.utils.datastructures import MultiValueDictKeyError

from recipeSite.models import Ingredient


def sort_recipes(recipeList, request):
    
    try:
        sort_value=request.GET['sort']

        if (sort_value=="trending"):
            recipeList = recipeList.order_by('-likes')
        if (sort_value=="latest"):
            recipeList = recipeList.order_by('-submissionDateTime')
        if (sort_value=="oldest"):
            recipeList = recipeList.order_by('submissionDateTime')
        if (sort_value=="cookTime"):
            recipeList = recipeList.order_by('cookTime')
        if (sort_value=="servings"):
            recipeList = recipeList.order_by('-servings')
    
    except MultiValueDictKeyError: #no get request called 'sort' was sent
        recipeList = recipeList.order_by('-likes') #just default to most likes
    
    return recipeList

def browseRecipe(request):

    AllrecipeList=sort_recipes(Recipe.objects.all(),request)
    
    return render(request, 'recipeSite/browseRecipe.html',
            context = {'recipeList' : AllrecipeList})

@login_required
def myRecipes(request):

    userRecipeList=sort_recipes(Recipe.objects.filter(author=request.user),request)

    return render(request, 'recipeSite/myRecipes.html',
            context = {'recipeList' : userRecipeList})

@login_required
def savedRecipes(request):

    bookmarkedRecipeList=sort_recipes(Recipe.objects.filter(bookmarks=request.user),request) #get all recipes that have been bookmarked by this user
   
    return render(request, 'recipeSite/savedRecipes.html',
            context = {'recipeList' : bookmarkedRecipeList})


class AddRecipe(View):

    @method_decorator(login_required)
    def get(self, request):
        form=RecipeForm()
        return render(request, 'recipeSite/addRecipe.html',context =  {'form' : form})

    @method_decorator(login_required)
    def post(self,request):

        form=RecipeForm(request.POST,request.FILES)

        if form.is_valid():

            recipe=form.save(commit=False)
            recipe.author= request.user #associate this recipe with the user who is logged in when this request was made 
            recipe.save()
            
            ingredients=request.POST.getlist('ingredients_arr[]')
            for ingredient in ingredients: #create a new ingredient in the database for every list item added by the user
                ingred = Ingredient.objects.get_or_create(recipe=recipe,ingredientName=ingredient)[0]
                ingred.save()

            return JsonResponse({
                'success': True,
                'url': reverse('recipeSite:viewRecipe',kwargs={'recipe_name_slug': recipe.slug}),
            })

        else:
            print(form.errors)
            html = render_to_string('recipeSite/addRecipe.html',context =  {'form' : form})
            return JsonResponse({
                'success': False,
                'html': html,
            })

def getRecipe(recipe_name_slug):
        context_dict={}
        try:
            recipe = Recipe.objects.get(slug=recipe_name_slug)
            ingredients = Ingredient.objects.filter(recipe=recipe)
            comments = Comments.objects.filter(recipe=recipe)
            context_dict['recipe'] = recipe
            context_dict['ingredients'] = ingredients
            context_dict['comments'] = comments

        except Recipe.DoesNotExist: 
            context_dict['recipe'] = None
            context_dict['ingredients'] = None
            context_dict['comments'] = None

        return context_dict

class editRecipe(View):

    @method_decorator(login_required)
    def get(self, request,recipe_name_slug):

        context_dict=getRecipe(recipe_name_slug)

        if (context_dict['recipe'].author == request.user):
            form = RecipeForm(instance=context_dict['recipe'])
            context_dict['form'] = form
            return render(request, 'recipeSite/addRecipe.html', context=context_dict)

        else:
            return HttpResponse("You are not allowed to edit this page.")

    @method_decorator(login_required)
    def post(self,request,recipe_name_slug):
        context_dict=getRecipe(recipe_name_slug)
        
        if (context_dict['recipe'].author == request.user):

            form=RecipeForm(request.POST,request.FILES,instance=context_dict['recipe'])
            
            if form.is_valid():

                recipe=form.save(commit=True) 
                
                ingredients=request.POST.getlist('ingredients_arr[]')
                print(ingredients)

                Ingredient.objects.filter(recipe=recipe).delete() #delete current ingredients for this recipe
                
                for ingredient in ingredients: #create new ingredients
                    ingred = Ingredient.objects.get_or_create(recipe=recipe,ingredientName=ingredient)[0]
                    ingred.save()

                return JsonResponse({
                    'success': True,
                    'url': reverse('recipeSite:viewRecipe',kwargs={'recipe_name_slug': recipe.slug}),
                })

            else:
                print(form.errors)
                html = render_to_string('recipeSite/addRecipe.html',context =  {'form' : form})
                return JsonResponse({
                    'success': False,
                    'html': html,
                })
        
        else:
            return HttpResponse("You are not allowed to edit this page.")

class viewRecipe(View):

    def get(self, request,recipe_name_slug):
        context_dict=getRecipe(recipe_name_slug)
        return render(request, 'recipeSite/viewRecipe.html', context=context_dict)

class ProfileView(View):
    def get_user_details(self, username):
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return None

        recipeList = Recipe.objects.filter(author=user)

        return (user, recipeList)

    def get(self, request, username):
        if (username == str(request.user)): #if user clicks on their own recipe, just link back to the myRecipes page
            return redirect(reverse('recipeSite:myRecipes'))
            
        else:
            try:
                (user, recipeList) = self.get_user_details(username)
            
            except TypeError:
                return redirect(reverse('recipeSite:index'))

            context_dict = {'selected_user': user,'recipeList': recipeList}

            return render(request, 'recipeSite/profile.html', context_dict)


class BookmarkRecipeView(View):
    @method_decorator(login_required)
    def get(self, request):

        recipeID=request.GET['recipe_id']

        try:
            recipe = Recipe.objects.get(id=int(recipeID))

        except recipe.DoesNotExist:
            return HttpResponse(-1)
        
        except ValueError:
            return HttpResponse(-1)

        if (recipe.bookmarks.filter(id=request.user.id).exists()): #check if the user has already bookmarked the recipe; if so they want to remove the bookmark
            recipe.bookmarks.remove(request.user)
            return HttpResponse("Deleted")
        else:
            recipe.bookmarks.add(request.user) #otherwise, they want to add the bookmark
            return HttpResponse("Bookmarked")

class DeleteRecipeButton(View):
    @method_decorator(login_required)
    def get(self, request):

        recipeID=request.GET['recipe_id']

        try:
            recipe = Recipe.objects.get(id=int(recipeID))

        except recipe.DoesNotExist:
            return HttpResponse(-1)
        
        except ValueError:
            return HttpResponse(-1)

        recipe.delete()
        return HttpResponse("Deleted")
        
@login_required
def myAccount(request):
    return render(request, 'recipeSite/myAccount.html',
            context =  {
            })

class deleteAccount(View):

    @method_decorator(login_required)
    def get(self, request):

        return render(request, 'registration/deleteAccount.html',
            context =  {
            })


    @method_decorator(login_required)
    def post(self, request):

        if (request.POST.get("delete")):

            User.objects.get(username=request.user.username).delete()

            logout(request)

            return redirect(reverse('recipeSite:browseRecipes'))
            
        elif(request.POST.get("cancel")):
                
            return redirect(reverse('myAccount'))

class LikeCategoryView(View):
    
    def get(self, request):
        recipeID = request.GET['recipe_id']
        try:
            recipe = Recipe.objects.get(id=int(recipeID))
        
        except Recipe.DoesNotExist:
            return HttpResponse(-1)
        except ValueError:
            return HttpResponse(-1)
        
        recipe.likes = recipe.likes + 1
        recipe.save()
        return HttpResponse(recipe.likes)
