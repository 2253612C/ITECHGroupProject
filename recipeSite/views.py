from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from recipeSite.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required
from recipeSite.forms import *


def about(request):
    return HttpResponse("This is the about page")

def browseRecipe(request):
    return render(request, 'recipeSite/browse.html',
            context =  {
            })
@login_required
def addRecipe(request):

    form=RecipeForm()

    if request.method == 'POST':
        form=RecipeForm(request.POST,request.FILES)

        if form.is_valid():

            form.save(commit=True)

            return redirect('browseRecipes') #should be changed to view recipe page once that is complete

        else:
            print(form.errors)

    return render(request, 'recipeSite/addRecipe.html',context =  {'form' : form})


@login_required
def myRecipes(request):
   return render(request, 'recipeSite/myRecipes.html',
            context =  {
            })
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
