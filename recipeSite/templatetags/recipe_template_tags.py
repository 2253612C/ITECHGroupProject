from django import template


register = template.Library()


@register.inclusion_tag('recipeSite/recipeCard.html')
def draw_recipe_cards(recipeList, user, can_edit_delete=False):
    return {'recipeList' : recipeList, 'user':user, 'can_edit_delete' : can_edit_delete}


@register.inclusion_tag('recipeSite/recipeCard.html')
def draw_recipe_cards_from_haystack(page_object_list, user):
    recipeList=[x.object for x in page_object_list] #get underlying model objects from haystack SearchResult objects
    return {'recipeList' : recipeList, 'user':user}

@register.filter
def has_bookmarked(user, recipe,):
    return recipe.bookmarks.filter(id=user.id).exists() #checks if user has bookmarked a recipe