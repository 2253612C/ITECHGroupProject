from unicodedata import category
from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username


class Recipe(models.Model):
    recipeName =  models.CharField(max_length=50)
    category =  models.CharField(max_length=20)
    description = models.TextField(max_length=500)
    method = models.TextField(max_length=500)
    cookTime = models.CharField(max_length=20)
    Servings = models.CharField(max_length=20)
    Difficutly = models.IntegerField(max_length=20)
    def __str__(self):
        return self.recipeName
    
class Comments(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    #whose_comment
    submissionDateTime = models.DateTimeField()
    content = models.TextField(max_length=500)

    def __str__(self):
        return self.submissionDateTime

class Ingredient(models.Model):
    ingredientName = models.CharField(max_length=50)

    def __str__(self):
        return self.ingredientName
