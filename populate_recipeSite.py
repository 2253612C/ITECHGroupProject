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
        {'submissionDateTime':'2022-03-13',
        'author' : user2,
        'content':'I have made this recipe twice and it is really tasty. Everyone loves it. Now I am making it again. This time with a Morello cherry compote topping.'},
        {'submissionDateTime':'2022-03-14',
        'author' : user3,
        'content':'Is it possible to make this ahead of time and refrigerate for a day or two? Or should this be made on the day only?'},
    ]

    
    Roasted_aubergine_tomato_curry_comments = [
        {'submissionDateTime':'2022-03-17',
        'author' : user2,
        'content':'May I use normal cow milk instead of coconut milk?? Thank you'},
        {'submissionDateTime':'2022-03-18',
        'author' : user3,
        'content':'I added double the amount of spice and ginger - will make again. '},
    ]

    cookie_comments = [
        {'submissionDateTime':'2022-03-17',
        'author' : user2,
        'content':"These were ok, but came out very cakey in texture. It's good if you like cakey cookies but we prefer ours soft & chewy."},
        {'submissionDateTime':'2022-03-18',
        'author' : user3,
        'content':"Absolutely loved these cookies and so did the family, even though I used self raising flour by mistake! As well as chocolate chips, I added chopped hazelnuts. I'll definitely use this recipe again but with plain flour."},
    ]


    Cod_with_butter_bean_colcannon_comments = [
        {'submissionDateTime':'2022-03-14',
        'author' : user1,
        'content':'Just made this and it is absolutely delicious. I used brussel sprouts shredded very finely as I had loads that needed using up , will definitely make again'},
        {'submissionDateTime':'2022-03-15',
        'author' : user3,
        'content':'Love this recipe, so simple and tasty. I’ve made it many times, I use 1/2 a tin extra of beans!'},
    ]


    pancake_comments = [
        {'submissionDateTime':'2022-03-02',
        'author' : user1,
        'content':"This crepe recipe is so so easy..put all ingredients in bowl and mixed with balloon whisk, left to rest for over 1 hour, crepes turned out perfect."},
        {'submissionDateTime':'2022-03-04',
        'author' : user3,
        'content':"Made these, absolutely delicious!."},
    ]

    chinese_curry_comments = [
        {'submissionDateTime':'2022-03-11',
        'author' : user1,
        'content':"If you want more sauce, I'd suggest adding an extra Onion and a little more stock."},
        {'submissionDateTime':'2022-03-12',
        'author' : user3,
        'content':"Delicious recipe, easy to follow, thickened well. I used medium curry powder."},
    ]


    Tomato_penne_with_avocado_comments = [
        {'submissionDateTime':'2022-03-18',
        'author' : user2,
        'content':'Loved this. Halved everything for one and it was delicious. Will definitely make again'},
        {'submissionDateTime':'2022-03-18',
        'author' : user3,
        'content':'Really easy and perfect dinner for a family, super delicious too!'},
    ]

    slow_cooked_pork_comments = [
        {'submissionDateTime':'2022-03-16',
        'author' : user2,
        'content':'Do you put a lid on when it goes in the oven?'},
        {'submissionDateTime':'2022-03-17',
        'author' : user3,
        'content':'Absolutely superb, one of the best recipes I have tried, will definitely be making many more times'},
    ]

    tomato_soup_comments = [
        {'submissionDateTime':'2022-03-16',
        'author' : user2,
        'content':'Gorgeous soup. Kids, vegans and grandpa all loved it. Served with a simple salad and crusty bread for Sunday lunch. '},
        {'submissionDateTime':'2022-03-17',
        'author' : user3,
        'content':'Is this soup thick or smooth?'},
    ]

    recipes = {
        'lemon baked cheesecake': #source:https://www.bbcgoodfood.com/recipes/luscious-lemon-baked-cheesecake
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


        'Roasted aubergine & tomato curry': #source:https://www.bbcgoodfood.com/recipes/roasted-aubergine-tomato-curry
        {'comments':Roasted_aubergine_tomato_curry_comments,
         'author' : user1,
        'category':'vegan',
        'description':"Slightly sweet with added richness from the coconut milk, this simple vegan curry is a winner. It's also freezable if you need a quick midweek fix.",
        'method':'Heat oven to 200C/180C fan/gas 6. Toss the aubergines in a roasting tin with 2 tbsp olive oil, season well and spread out. Roast for 20 mins or until dark golden and soft.',
        'cookTime':45,
        'Servings':4,
        'difficulty':'EASY',
        'likes':11,
        'image':"recipeImages\\aubergine-tomato-curry.jpg",
        'ingredients' : { 'olive oil, 3tbsp','2 onions, finely sliced','2 garlic cloves, crushed','400ml can chopped tomatoes'},
        'submissionDateTime':'2022-03-07'
        },

        'Vintage chocolate chip cookies': #source:https://www.bbcgoodfood.com/recipes/vintage-chocolate-chip-cookies
        {'comments':cookie_comments,
         'author' : user1,
        'category':'cookies',
        'description':"An easy chocolate chip cookie recipe for soft biscuits with a squidgy middle that will impress family and friends. Make plenty as they're sure to be a hit.",
        'method':'Heat the oven to 190C/fan170C/gas 5 and line two baking sheets with non-stick baking paper. Put 150g softened salted butter, 80g light brown muscovado sugar and 80g granulated sugar into a bowl and beat until creamy. Bake for 8 to 10 mins until they are light brown on the edges and still slightly soft in the centre if you press them.',
        'cookTime':10,
        'Servings':30,
        'difficulty':'EASY',
        'likes':54,
        'image':"recipeImages\\vintage-cookies.png",
        'ingredients' : { '150g salted butter, softened','80g granulated sugar','2 tsp vanilla extract','1 large egg'},
        'submissionDateTime':'2022-03-02'
        },

        'Cod with butter bean colcannon': #source https://www.bbcgoodfood.com/recipes/cod-butter-bean-colcannon
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

        'Easy pancakes': #source https://www.bbcgoodfood.com/recipes/easy-pancakes
        {'comments':pancake_comments,
         'author' : user2,
        'category':'easy recipes',
        'description':"Learn a skill for life with our foolproof crêpe recipe that ensures perfect pancakes every time.",
        'method':"Put 100g plain flour, 2 large eggs, 300ml milk, 1 tbsp sunflower or vegetable oil and a pinch of salt into a bowl or large jug, then whisk to a smooth batter. Set aside for 30 mins to rest if you have time, or start cooking straight away. Set a medium frying pan or crêpe pan over a medium heat and carefully wipe it with some oiled kitchen paper. When hot, cook your pancakes for 1 min on each side until golden, keeping them warm in a low oven as you go.",
        'cookTime':20,
        'Servings':12,
        'difficulty': 'EASY',
        'likes':66,
        'image':"recipeImages\pancake.png",
        'ingredients' : { '100g plain flour','2 large eggs','300ml milk','1 tbsp sunflower or vegetable oil, plus a little extra for frying'},
        'submissionDateTime': '2022-02-27',
        },


        'Chinese chicken curry': #source https://www.bbcgoodfood.com/recipes/chinese-chicken-curry
        {'comments':pancake_comments,
         'author' : user2,
        'category':'curry',
        'description':"Cook an easy, healthy curry with just 15 minutes preparation. Serve this replica of your favourite takeaway dish with fluffy rice for a wholesome family meal.",
        'method':"Toss the chicken pieces in the cornflour and season well. Set them aside. Fry the onion in half of the oil in a wok on a low to medium heat, until it softens – about 5-6 minutes – then add the garlic and cook for a minute. Stir in the spices and sugar and cook for another minute, then add the stock and soy sauce, bring to a simmer and cook for 20 minutes. Tip everything into a blender and blitz until smooth. Wipe out the pan and fry the chicken in the remaining oil until it is browned all over. Tip the sauce back into the pan and bring everything to a simmer, stir in the peas and cook for 5 minutes. Add a little water if you need to thin the sauce. Serve with rice.",
        'cookTime':40,
        'Servings':4,
        'difficulty': 'MEDIUM',
        'likes':32,
        'image':"recipeImages\chicken-curry.jpg",
        'ingredients' : { '4 skinless chicken breasts, cut into chunks','2 tsp cornflour','1 onion, diced','1 garlic clove, crushed'},
        'submissionDateTime': '2022-03-09',
        },

        'Tomato penne with avocado': #source https://www.bbcgoodfood.com/recipes/mexican-penne-avocado
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
        },

        'Slow-cooked pork, cider & sage hotpot': #source https://www.bbcgoodfood.com/recipes/slow-cooked-pork-cider-sage-hotpot
        {'comments':slow_cooked_pork_comments,
         'author' : user3,
        'category':'slow-cooked',
        'description':"Warm up as the cold nights set in with this glorious hotpot, with slow-cooked pork cooked in cider and sage. It's topped with a crispy layer of potatoes",
        'method':"Heat half of the oil in a deep ovenproof frying pan, or flameproof casserole dish, and fry the pork pieces over a medium high heat in batches until seared all over, then transfer to a plate. \nAdd another 1 tbsp oil to the pan, if you need to, while you're cooking the batches. Once all the pork is seared, transfer to a plate and set aside. Add another 1 tbsp oil to the pan with a little butter and fry half the leeks with a pinch of salt for 10 mins until tender. Add the garlic, fry for a minute, then stir in the flour.\n Pour in the cider, a little at a time, stirring to pick up any bits stuck to the bottom of the pan and to combine everything. Add the stock, bay leaves and seared pork, then simmer, half-covered with a lid for 1-1½ hrs until the meat is just tender (it will later cook to the point of falling apart in the oven). Can be prepared a day ahead.",
        'cookTime':180,
        'Servings':6,
        'difficulty':'HARD',
        'likes':12,
        'image':"recipeImages\slow-cooked-pork-cider-sage.jpg",
        'ingredients' : {'4 tbsp olive oil, plus a little extra','1kg diced pork shoulder','500ml dry cider','400ml chicken stock'},
        'submissionDateTime':'2022-03-15',
        },

        'Tomato & basil soup': #source https://www.bbcgoodfood.com/recipes/rich-tomato-soup-pesto
        {'comments':tomato_soup_comments,
         'author' : user3,
        'category':'soup',
        'description':"Combine fruity sundried tomatoes with tinned tomatoes to make this rich tomato soup with a homemade basil pesto. Perfect for the depths of winter.",
        'method':"Heat the butter or oil in a large pan, then add the garlic and soften for a few minutes over a low heat. Add the sundried or SunBlush tomatoes, canned tomatoes, stock, sugar and seasoning, then bring to a simmer. Let the soup bubble for 10 mins until the tomatoes have broken down a little. Whizz with a stick blender, adding half the pot of soured cream as you go. Taste and adjust the seasoning – add more sugar if you need to. Serve in bowls with 1 tbsp or so of the pesto swirled on top, a little more soured cream and scatter with basil leaves.",
        'cookTime':15,
        'Servings':4,
        'difficulty':'EASY',
        'likes':45,
        'image':"recipeImages\\tomato-soup.jpg",
        'ingredients' : {'1 tbsp butter or olive oil','2 garlic cloves, crushed','3 x 400g cans plum tomatoes','500ml turkey or vegetable stock','125g pot fresh basil pesto'},
        'submissionDateTime':'2022-03-15',
        }
    }


    for recipe, recipe_data in recipes.items():
        rec = add_recipe(recipe, recipe_data)

        for ing in recipe_data['ingredients']:
            add_ingredient(ing,rec)

        for com in recipe_data['comments']:
            for comment in com:
                add_comments(rec, com['submissionDateTime'], com['content'],com['author'])




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

def add_comments(rec,submissionDateTime,content,author):
    c = Comments.objects.get_or_create(recipe=rec,author=author)[0]
    c.submissionDateTime = submissionDateTime
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
    print('Starting recipe population script...')
    populate()