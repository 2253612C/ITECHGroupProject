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

    category = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Ingredient(models.Model):
    ingredientName = models.CharField(max_length=50)

    def __str__(self):
        return self.ingredientName
