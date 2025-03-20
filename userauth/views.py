from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from .forms import CustomUserRegistrationForm

# Create your views here.

# function to handle user registration
def register_view(request):
    # if form is submitted
    if request.method == 'POST':
        form = CustomUserRegistrationForm(request.POST) # custom form with submitted data
        # validate form
        if form.is_valid():
            user = form.save() # save form
            login(request, user)  # Automatically logs in the user
            return redirect('homepage')  # Redirect to homepage
    else:
        form = CustomUserRegistrationForm() # form not submitted, display empty form
    
    return render(request, 'sign-up.html', {'form': form})

# function to handle user login 
def login_view(request):
     # if form is submitted
     if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST) # built-in authentication form with submitted data
        # validate form 
        if form.is_valid():
            # storing email & password
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password) # authenticate user
            
            # if user authentication was successful
            if user is not None:
                login(request, user) # login user
                return redirect('homepage')  # Redirect to homepage
        else:
            return render(request, 'login.html', {'form': form, 'error': 'Invalid credentials'}) # form not valid 
     else:
         form = AuthenticationForm() # form not submitted, display empty form
     return render(request, 'login.html', {'form': form})