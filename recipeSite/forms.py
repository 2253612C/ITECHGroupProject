from django import forms
from django.contrib.auth.models import User
from datetime import datetime
from recipeSite.models import UserProfile,Recipe,Comments

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
    recipeName =  forms.CharField(max_length=50, help_text="Please enter the recipe name.")
    category =  forms.CharField(max_length=20, help_text="Please enter the category name.")
    description = forms.TextField(max_length=500, help_text="Please enter the description.")
    method = forms.TextField(max_length=500, help_text="Please enter the method.")
    cookTime = forms.CharField(max_length=20, help_text="Please enter the cook time.")
    Servings = forms.CharField(max_length=20, help_text="Please enter the serving size.")
    Difficutly = forms.IntegerField(max_length=20,help_text="Please enter the difficulty.")
    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Category
        fields = ('recipeName','category','description','method','cookTime','Servings','Difficutly')


class CommentsForm(forms.ModelForm):
    submissionDateTime = forms.DateTimeField(default=datetime.now(), blank=True)
    content = forms.TextField(max_length=500, help_text="Please put your comments here.")
    #whose_comment
    class Meta:
        model = Comments
        fields = ('submissionDateTime', 'content',)
