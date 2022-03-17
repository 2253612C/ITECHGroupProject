from django import template


register = template.Library()


@register.inclusion_tag('recipeSite/recipeCard.html')
def draw_recipe_cards(recipeList, user):
    return {'recipeList' : recipeList, 'user':user}

@register.filter
def has_bookmarked(user, recipe):

    return recipe.bookmarks.filter(id=user.id).exists() #checks if user has bookmarked a recipe