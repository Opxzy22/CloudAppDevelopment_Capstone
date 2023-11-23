from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.forms import UserCreationForm
# from .models import related models
# from .restapis import related methods
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from datetime import datetime
import logging
import json
from .forms import SignUpForm

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
        # Step 1: Get form data
        form = UserCreationForm(request.POST)
        
        # Step 2: Check if the form is valid
        if form.is_valid():
            # Step 3: Extract cleaned data from the form
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']

            try:
                # Step 4: Check if user already exists
                existing_user = User.objects.get(username=username)
                logger.debug(f"{username} already exists.")
            except User.DoesNotExist:
                # Step 5: If not, create a new user
                logger.debug(f"{username} is a new user.")
                user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,
                                                password=password)
                # Step 6: Log in the user after successful signup
                login(request, user)
                return redirect('django:index')

    else:
        # Step 7: If it's not a POST request, create an empty form
        form = UserCreationForm()

    # Step 8: Render the registration page with the form
    return render(request, 'djangoapp/registration.html', {'form': form})
# ...

# Update the `get_dealerships` view to render the index page with a list of dealerships
def get_dealerships(request):
    context = {}
    if request.method == "GET":
        return render(request, 'djangoapp/index.html', context)


# Create a `get_dealer_details` view to render the reviews of a dealer
# def get_dealer_details(request, dealer_id):
# ...

# Create a `add_review` view to submit a review
# def add_review(request, dealer_id):
# ...

