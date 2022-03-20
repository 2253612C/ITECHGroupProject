from django.contrib import admin
from recipeSite.models import *


class recipeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('recipeName',)}


admin.site.register(Recipe,recipeAdmin)
admin.site.register(Ingredient)
admin.site.register(Comments)