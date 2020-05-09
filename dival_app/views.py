from django.shortcuts import render
from dival_app.models import UserProfile
from .forms import LoginForm,RegistrationForm

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    registered = False

    if request.method == 'POST':

        registration_form = RegistrationForm(data=request.POST)

        if registration_form.is_valid():
            registration_form.save(commit=False)


            if 'picture' in request.FILES:
                registration_form.picture = request.FILES['picture']

            registration_form.save()
            registered = True

        else:
            print(registration_form.errors)
    else:
        registration_form = RegistrationForm()


    return render(request,'index.html',{'registrationform':registration_form,'registered':registered})

    # return render(request,'index.html')


def register(request):
    return render(request,'register.html')





def login(request):

    if request.method == 'POST':
        # First get the username and password supplied
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Django's built-in authentication function:
        user = authenticate(username=username, password=password)

        # If we have a user
        if user:
            #Check it the account is active
            if user.is_active:
                # Log the user in.
                login(request,user)
                # Send the user back to some page.
                # In this case their homepage.
                return HttpResponseRedirect(reverse('index'))
            else:
                # If account is not active:
                return HttpResponse("Your account is not active.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details supplied.")

    else:
        #Nothing has been provided for username or password.
        return render(request, 'login.html', {})


@login_required
def special(request):
    # Remember to also set login url in settings.py!
    # LOGIN_URL = '/basic_app/user_login/'
    return HttpResponse("You are logged in..")

@login_required
def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return HttpResponseRedirect(reverse('index'))



def login_user(request):
    if request.method == 'POST':
        login_form = LoginForm(data=request.POST)
        if login_form.is_valid():
            login_form.save()
        else:
            print(login_form.errors)
    else:
        login_form = LoginForm()
    return render(request,'thanku.html',{'login_form':login_form})
