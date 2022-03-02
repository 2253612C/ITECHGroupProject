from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("This is the homepage")

def about(request):
    return HttpResponse("This is the about page")

def login(request):
    return HttpResponse("This is the login page ")

def register(request):
    return HttpResponse("This is the register page")

def browseRecipe(request):
    return HttpResponse("This is the browse page")

def addRecipe(request):
    return HttpResponse("This is the add recipe page")
