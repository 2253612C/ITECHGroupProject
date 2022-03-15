from django import forms
from django.contrib.auth.models import User
from datetime import datetime
from recipeSite.models import UserProfile,Recipe,Comments
from django.db import models
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture',)


class RecipeForm(forms.ModelForm):
    recipeName =  forms.CharField(label="Name Your Recipe",max_length=50, help_text="Please enter the recipe name.")
    category =  forms.CharField(label="Category",max_length=20, help_text="Please enter the category name.")
    description = forms.CharField(label="Add a short description.",max_length=250, help_text="Please enter the description.",widget=forms.Textarea(attrs={'rows':2})) #was textfield
    method = forms.CharField(label="Add a method",max_length=500, help_text="Please enter the method.",widget=forms.Textarea(attrs={'rows':2})) #was textfield
    cookTime = forms.DurationField(label="Cook Time",help_text="Please enter the cook time.")
    servings = forms.IntegerField(label="Serving Size",help_text="Please enter the serving size.",min_value=1,max_value=12)
    difficulty = forms.ChoiceField(label="Difficulty",choices=Recipe.RECIPE_DIFFICULTY,help_text="Please enter the difficulty.")
    image=  forms.ImageField(label="Add an Image")
    likes = forms.IntegerField(widget=forms.HiddenInput(), required= False, initial=0)


    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Recipe
        fields = ('recipeName','category','description','method','cookTime','servings','difficulty','likes','image')
        widgets = {
        'cookTime' : forms.DurationField,
        'difficulty': forms.Select(),
        
        #'recipeName':forms.TextInput( attrs={ 'class': 'form-control', 'placeholder': 'Title', 'required': True, } ),
        
        }

    



class CommentsForm(forms.ModelForm):
    submissionDateTime = forms.DateTimeField() #default=datetime.now(), blank=True
    content = forms.CharField(max_length=500, help_text="Please put your comments here.") #was txt field
    #whose_comment
    class Meta:
        model = Comments
        fields = ('submissionDateTime', 'content',)
