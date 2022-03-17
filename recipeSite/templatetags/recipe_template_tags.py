from django import template


register = template.Library()


@register.inclusion_tag('recipeSite/recipeCard.html')
def draw_recipe_cards(recipeList):
    return {'recipeList' : recipeList}