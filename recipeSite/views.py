from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from recipeSite.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required


def about(request):
    return HttpResponse("This is the about page")

def browseRecipe(request):
    return render(request, 'recipeSite/browse.html',
            context =  {
            })
@login_required
def addRecipe(request):
   return render(request, 'recipeSite/addRecipe.html',
            context =  {
            })
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
