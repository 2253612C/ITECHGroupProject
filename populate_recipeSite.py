import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                        'ITECHGroupProject.settings')

import django
django.setup()

from recipeSite.models import Recipe, Comments, Ingredient
from django.contrib.auth.models import User
from django.utils import timezone
import datetime


def populate(): 

    user1=create_user("user_1",'123')
    user2=create_user("user_2",'123')
    user3=create_user("user_3",'123')

    lemon_baked_cheesecake_comments = [
        {'submissionDateTime':'23:24:13',
        'content':'I have made this recipe twice and it is really tasty. Everyone loves it. Now I am making it again. This time with a Morello cherry compote topping.'},
        {'submissionDateTime':'12:43:53',
        'content':'Is it possible to make this ahead of time and refrigerate for a day or two? Or should this be made on the day only?'},
    ]

    Cod_with_butter_bean_colcannon_comments = [
        {'submissionDateTime':'18:43:57',
        'content':'Just made this and it is absolutely delicious. I used brussel sprouts shredded very finely as I had loads that needed using up , will definitely make again'},
        {'submissionDateTime':'07:33:27',
        'content':'Love this recipe, so simple and tasty. I’ve made it many times, I use 1/2 a tin extra of beans!'},
    ]

    Tomato_penne_with_avocado_comments = [
        {'submissionDateTime':'14:54:33',
        'content':'what else can I use instead of red pepper?'},
        {'submissionDateTime':'09:05:22',
        'content':'Loved this. Halved everything for one and it was delicious. Will definitely make again'},
        {'submissionDateTime':'22:15:52',
        'content':'Really easy and perfect dinner for a family, super delicious too!'},
    ]

    

    recipes = {
        'lemon baked cheesecake':
        
        {'comments':lemon_baked_cheesecake_comments,
         'author' : user1,
        'category':'Dessert',
        'description':'A simple but very impressive pud, light enough to have a slice to finish a big meal.',
        'method':'Heat oven to 180C/fan 160C/gas 4. Line the bottom of a 23cm springform tin with greaseproof paper. Tip the biscuits and melted butter into a food processor, then blitz to make fine crumbs. Press into the tin and chill.',
        'cookTime':40,
        'Servings':10,
        'difficulty':'MEDIUM',
        'likes':23,
        'image':"recipeImages\lemon.jpg",
        'ingredients' : { 'icing sugar, 25g','digestive biscuits 250g','butter, 100g melted',},
        'submissionDateTime':'2022-03-12'
                        
        },

        'Cod with butter bean colcannon':
        {'comments':Cod_with_butter_bean_colcannon_comments,
         'author' : user2,
        'category':'Seafood',
        'description':'Whip up a budget-friendly fish dinner with creamy butter bean colcannon. It is the perfect midweek meal for two and ready in just 15 minutes',
        'method':'Heat oven to 220C/200C fan/gas 8. Cut two squares of baking parchment slightly bigger than the cod and place a fillet in the centre of each one. Divide 20g of the butter between the two fillets and top with a few thyme leaves and lemon slices. Season generously. Fold and scrunch the paper together to create two paper parcels. Put on a baking sheet and cook for 8-10 mins.',
        'cookTime':10,
        'Servings':2,
        'difficulty': 'EASY',
        'likes':54,
        'image':"recipeImages\colcannon.jpg",
        'ingredients' : { 'cod fillet, 2','butter, 200g'},
        'submissionDateTime': '2022-03-14',
        },
        
        'Tomato penne with avocado':
        {'comments':Tomato_penne_with_avocado_comments,
         'author' : user3,
        'category':'Vegetarian',
        'description':'Get all five of your 5-a-day in this mildly spiced, healthy pasta dish. It is rich in iron, fibre and vitamin C as well as being low-fat and low-calorie',
        'method':'Cook the pasta in salted water for 10-12 mins until al dente. Meanwhile, heat the oil in a medium pan. Add the sliced onion and pepper and fry, stirring frequently for 10 mins until golden. Stir in the garlic and spices, then tip in the tomatoes, half a can of water, the corn and bouillon. Cover and simmer for 15 mins.',
        'cookTime':20,
        'Servings':2,
        'difficulty':'EASY',
        'likes':33,
        'image':"recipeImages\\avocado.jpg",
        'ingredients' : {'tomato, 14 oz crushed','avocado, 1 stoned and chopped','pasta, 1/2 lb'},
        'submissionDateTime':'2022-03-17',
        }
    }

    print(recipes["Cod with butter bean colcannon"])

    for recipe, recipe_data in recipes.items():
        rec = add_recipe(recipe, recipe_data)
        
        for ing in recipe_data['ingredients']:
            add_ingredient(ing,rec)   
        
        for com in recipe_data['comments']:
            for comment in com:
                add_comments(rec, com['submissionDateTime'], com['content'])

    


def add_recipe(name,recipe_data):
    r = Recipe.objects.get_or_create(recipeName=name,author=recipe_data['author'])[0]
    r.category=recipe_data['category']
    r.description=recipe_data['description']
    r.method=recipe_data['method']
    r.cookTime=recipe_data['cookTime']
    r.servings=recipe_data['Servings']
    r.difficulty=recipe_data['difficulty']
    r.likes=recipe_data['likes']
    r.image= recipe_data['image']
    r.submissionDateTime = recipe_data['submissionDateTime']
    r.save()
    return r

def add_comments(rec,submissionDateTime,content):
    c = Comments.objects.get_or_create(recipe=rec)[0]
    c.submissionDateTime = timezone.now()
    c.content = content
    c.save()
    return c

def add_ingredient(name,recipe):
    i=Ingredient.objects.get_or_create(ingredientName=name,recipe=recipe)[0]
    i.save()
    return i

def create_user(username,password):
    user,created = User.objects.get_or_create(
        username=username)

    if (created):
        user.set_password(password)
        user.save()
    
    return user

if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()