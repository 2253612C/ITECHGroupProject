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
        sort_value=request.GET['sort'] #sort parameter for viewing recipes 

        if (sort_value=="mostPopular"):
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

    AllrecipeList=sort_recipes(Recipe.objects.all(),request) #get all recipes for the browse recipe page
    
    return render(request, 'recipeSite/browseRecipe.html',
            context = {'recipeList' : AllrecipeList})

@login_required
def myRecipes(request):

    userRecipeList=sort_recipes(Recipe.objects.filter(author=request.user),request) #get recipes submitted by the user making this request

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

            return JsonResponse({ #send json response back to ajax post 
                'success': True,
                'url': reverse('recipeSite:viewRecipe',kwargs={'recipe_name_slug': recipe.slug}), #redirect to the view recipe page after submission
            })

        else:
            print(form.errors)
            html = render_to_string('recipeSite/addRecipe.html',context =  {'form' : form}) #render the form again with errors
            return JsonResponse({
                'success': False,
                'html': html,
            })

def getRecipe(recipe_name_slug):
        context_dict={}
        try:
            recipe = Recipe.objects.get(slug=recipe_name_slug) #get the recipe associated with the slug
            ingredients = Ingredient.objects.filter(recipe=recipe) #get ingredients and comments
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

        form=CommentsForm()
        context_dict['form']=form

        return render(request, 'recipeSite/viewRecipe.html', context=context_dict)

    @method_decorator(login_required)
    def post(self,request,recipe_name_slug):

        form=CommentsForm(request.POST) #create a form to make a comment

        if form.is_valid():

            context_dict=getRecipe(recipe_name_slug)

            comment=form.save(commit=False)
            comment.author=request.user #save the author of the comment 
            comment.recipe=context_dict['recipe']
            comment.save()

            

            return render(request, 'recipeSite/viewRecipe.html', context=context_dict) #redisplay the page with the added comment 

        else:
            return redirect(reverse('recipeSite:browseRecipes'))


class ProfileView(View):
    def get_user_details(self, username):
        try:
            user = User.objects.get(username=username) #get user object associated with the username
        except User.DoesNotExist:
            return None

        recipeList = Recipe.objects.filter(author=user) #get the recipes submitted by that user

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


class BookmarkRecipeView(View): #view used to process ajax post when user clicks to bookmark a recipe
    @method_decorator(login_required)
    def get(self, request):

        recipeID=request.GET['recipe_id']

        try:
            recipe = Recipe.objects.get(id=int(recipeID)) #get the recipe they bookmarked

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

class DeleteRecipeButton(View):  #view used to process ajax post when user clicks to delete a submitted recipe
    @method_decorator(login_required)
    def get(self, request):

        recipeID=request.GET['recipe_id']

        try:
            recipe = Recipe.objects.get(id=int(recipeID))  #get recipe using id

        except recipe.DoesNotExist:
            return HttpResponse(-1)
        
        except ValueError:
            return HttpResponse(-1)

        recipe.delete() #remove from database
        return HttpResponse("Deleted")

class DeleteCommentButton(View):  #view used to process ajax post when user clicks to delete a submitted comment
    @method_decorator(login_required)
    def get(self, request):

        commentID=request.GET['comment_id'] #get comment by ID

        try:
            comment = Comments.objects.get(id=int(commentID))
            print(comment.content)

        except comment.DoesNotExist:
            print("failure")
            return HttpResponse(-1)
        
        except ValueError:
            print("failure2")
            return HttpResponse(-1)

        comment.delete()
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

            logout(request) #log user out first

            return redirect(reverse('recipeSite:browseRecipes')) #redirect to homepage after user deletes accoount
            
        elif(request.POST.get("cancel")):
                
            return redirect(reverse('myAccount')) #redirect back to account page if they cancel

class LikeCategoryView(View): #view used to process ajax get when user likes a recipe
    
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
