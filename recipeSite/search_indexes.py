import datetime
from haystack import indexes
from .models import Recipe


class RecipeIndex(indexes.SearchIndex, indexes.Indexable):  
    text = indexes.CharField(document=True, use_template=True)  

    def get_model(self): 
        return Recipe

    def index_queryset(self, using=None): 
        """Used when the entire index for model is updated."""
        # return self.get_model().objects.filter(updated__lte=datetime.datetime.now())
        return self.get_model().objects.all()