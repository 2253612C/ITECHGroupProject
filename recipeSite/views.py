from django.shortcuts import render
from django.http import HttpResponse
from recipeSite.forms import UserForm, UserProfileForm


def index(request):
     return HttpResponse("This is index page")

def home(request):
    return HttpResponse("This is the homepage")

def about(request):
    return HttpResponse("This is the about page")

def login(request):
    return render(request, 'recipeSite/login.html')

def register(request):
    
    registered=False

    if request.method == 'POST':


        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user =user_form.save()

            user.set_password(user.password)
            user.save()


            profile = profile_form.save(commit=False)
            profile.user = user


            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()


            registered = True
        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'recipeSite/register.html',
            context =  {'user_form' : user_form, 
                        'profile_form ': profile_form,
                        'registered' : registered}
                  )

def browseRecipe(request):
    return HttpResponse("This is the browse page")

def addRecipe(request):
    return HttpResponse("This is the add recipe page")
