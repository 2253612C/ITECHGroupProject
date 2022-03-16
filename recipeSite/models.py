from this import d
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
import datetime
from django.utils import timezone


class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username


class Recipe(models.Model):
    EASY='EASY'
    MEDIUM='MEDIUM'
    HARD='HARD'
        
    RECIPE_DIFFICULTY=[
    (EASY, 'Easy to Make'),
    (MEDIUM, 'Moderately Difficult'),
    (HARD, 'Hard to Make'),
    ]

    recipeName =  models.CharField(max_length=50, unique=True)
    category =  models.CharField(max_length=20)
    description = models.TextField(max_length=500)
    method = models.TextField(max_length=500)
    cookTime = models.IntegerField(default=0)
    difficulty = models.CharField(max_length=6 ,
                                  choices=RECIPE_DIFFICULTY,
                                   default=EASY)
    servings = models.PositiveIntegerField(default=0)
    likes=models.IntegerField(default=0)
    image=  models.ImageField(upload_to='recipeImages',blank=True)
    slug=models.SlugField()
    

    def save(self, *args, **kwargs):
        self.slug = slugify(self.recipeName)
        super(Recipe, self).save(*args, **kwargs)

    def __str__(self):
        return self.recipeName
    
class Comments(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    #whose_comment
    submissionDateTime = models.DateTimeField(default=timezone.now)
    content = models.TextField(max_length=500)

    def __str__(self):
        return self.content

class Ingredient(models.Model):
    recipe=models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredientName = models.CharField(max_length=50)

    def __str__(self):
        return self.ingredientName
