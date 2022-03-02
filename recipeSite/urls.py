from django.urls import path
from recipeSite import views

app_name = 'recipeSite'

urlpatterns = [
   path('', views.index, name= 'index'),
]