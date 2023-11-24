from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.forms import UserCreationForm
# from .models import related models
# from .restapis import related methods
from .restapis import get_dealers_from_cf, get_dealers_by_state
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from datetime import datetime
import logging
import json
#from .form import SignUpForm

# Get an instance of a logger
logger = logging.getLogger(__name__)


# Create your views here.
def my_view(request):
    return render(request, 'template.html')

# Create an `about` view to render a static about page
def about(request):
    return render(request, 'about.html')


# ...


# Create a `contact` view to return a static contact page
def contact(request):
    return render(request, 'contact.html')

# Create a `login_request` view to handle sign in request
from django.contrib.auth.forms import AuthenticationForm

def login_request(request):
    if request.method == "POST":
        # Use Django's built-in AuthenticationForm for form validation
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # The form data is valid, proceed with authentication
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            # Authenticate user
            user = authenticate(request, username=username, password=password)

            if user is not None:
                # Login the user
                login(request, user)
                messages.success(request, 'Login successful.')
                return redirect('django:index')  # Adjust the redirect path
            else:
                messages.error(request, 'Invalid password or username')
        else:
            messages.error(request, 'Form is not valid. Please check your input.')
    
    # If the request is not POST or form is not valid, render the login template
    return render(request, 'login.html')

# ...

# Create a `logout_request` view to handle sign out request
def logout_request(request):
    # use django's logout function to logout user
    logout(request)
    # add a logout success message
    messages.success(request, 'you have logout successfully.')
    # redirect to the login page after logout
    return redirect ('login')
# ...

# Create a `registration_request` view to handle sign up request
def registration_request(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user after successful signup
            return redirect ('django/index.html')
    else:
        form = UserCreationForm()
    return render(request, 'djangoapp/registration.html', {'form': form})

   
# Update the `get_dealerships` view to render the index page with a list of dealerships
def get_dealerships(request):
    if request.method == "GET":
        url = "https://us-south.functions.appdomain.cloud/api/v1/web/a12ecb5a-f0a3-4a55-9a4a-b1b28c1fdc99/default/getDealerships"
        # Get dealers from the URL
        dealerships = get_dealers_from_cf(url)
        # Concat all dealer's short name
        dealer_names = ' '.join([dealer.short_name for dealer in dealerships])
        # Return a list of dealer short name
        return HttpResponse(dealer_names)


def get_dealershps_by_state(request, state):
    if request.method == "GET":
        url = "https://us-south.functions.appdomain.cloud/api/v1/web/a12ecb5a-f0a3-4a55-9a4a-b1b28c1fdc99/default/getDealerships"
        # get dealers by state from url
        dealership_by_state = get_dealers_by_state(url, state)
        return HttpResponse(dealership_by_state)


# Create a `get_dealer_details` view to render the reviews of a dealer
# def get_dealer_details(request, dealer_id):
# ...

# Create a `add_review` view to submit a review
# def add_review(request, dealer_id):
# ...

