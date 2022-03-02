from django.urls import path
from recipeSite import views

app_name = 'recipeSite'

urlpatterns = [
    path('', views.home, name= 'home'),
]