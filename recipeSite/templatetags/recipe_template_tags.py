from django import template


register = template.Library()


@register.inclusion_tag('recipeSite/recipeCard.html')
def draw_recipe_cards(recipeList, user, can_edit_delete=False):
    return {'recipeList' : recipeList, 'user':user, 'can_edit_delete' : can_edit_delete}

@register.filter
def has_bookmarked(user, recipe,):

    return recipe.bookmarks.filter(id=user.id).exists() #checks if user has bookmarked a recipe