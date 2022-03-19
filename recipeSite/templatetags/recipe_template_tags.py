from django import template


register = template.Library()

#template tag which draws a number of recipe cards on a page, given a list of recipes (should be sorted as required in the views)
#pass in an additional boolean arguement to also display the edit and delete buttons
@register.inclusion_tag('recipeSite/recipeCard.html')
def draw_recipe_cards(recipeList, user, can_edit_delete=False):
    return {'recipeList' : recipeList, 'user':user, 'can_edit_delete' : can_edit_delete}

#same as above, but converts haystack search results into recipe objects from databse first
@register.inclusion_tag('recipeSite/recipeCard.html')
def draw_recipe_cards_from_haystack(page_object_list, user):
    recipeList=[x.object for x in page_object_list] #get underlying model objects from haystack SearchResult objects
    return {'recipeList' : recipeList, 'user':user}

#filter tag to check in html templates if the user has bookmarked a recipe
@register.filter
def has_bookmarked(user, recipe,):
    return recipe.bookmarks.filter(id=user.id).exists() #checks if user has bookmarked a recipe