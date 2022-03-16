from django.shortcuts import render,redirect,reverse
from django.template.loader import render_to_string
from django.http import HttpResponse
from recipeSite.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required
from recipeSite.forms import *
from django.http import JsonResponse
from django.views import View

from recipeSite.models import Ingredient

def about(request):
    return HttpResponse("This is the about page")

def browseRecipe(request):
    Recipe_list = Recipe.objects.order_by('-likes')[:3]

    return render(request, 'recipeSite/browseRecipe.html',
            context = {'Recipe_list' : Recipe_list})

@login_required
def addRecipe(request):

    form=RecipeForm()

    if request.method == 'POST':
        form=RecipeForm(request.POST,request.FILES)

        if form.is_valid():

            recipe=form.save(commit=True)
            ingredients=request.POST.getlist('ingredients_arr[]')
           
            print(ingredients)

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


    return render(request, 'recipeSite/addRecipe.html',context =  {'form' : form})

class viewRecipe(View):

    def getRecipe(self,context_dict,recipe_name_slug):
        try:

            recipe = Recipe.objects.get(slug=recipe_name_slug)
            ingredients = Ingredient.objects.filter(recipe=recipe)
        
            context_dict['recipe'] = recipe
            context_dict['ingredients'] = ingredients

        except Recipe.DoesNotExist:
        
            context_dict['recipe'] = None
            context_dict['ingredients'] = None

    def get(self, request,recipe_name_slug):
        context_dict ={}
        self.getRecipe(context_dict,recipe_name_slug)
        return render(request, 'recipeSite/viewRecipe.html', context=context_dict)


@login_required
def myRecipes(request):
    Recipe_list = Recipe.objects.all()

    return render(request, 'recipeSite/myRecipes.html',
            context = {'Recipe_list' : Recipe_list})

@login_required
def savedRecipes(request):
  return render(request, 'recipeSite/savedRecipes.html',
            context =  {
            })
@login_required
def myAccount(request):
    return render(request, 'recipeSite/myAccount.html',
            context =  {
            })

def restricted(request):
    return HttpResponse("You have to be a registered user to view this page")
