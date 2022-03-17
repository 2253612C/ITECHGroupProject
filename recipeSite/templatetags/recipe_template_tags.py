from django import template


register = template.Library()


@register.inclusion_tag('recipeSite/recipeCard.html')
def draw_recipe_cards(recipeList, user):
    return {'recipeList' : recipeList, 'user':user}