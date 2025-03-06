from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserRegistrationForm

# Create your views here.

# function to handle user registration
def register_view(request):
    if request.method == 'POST':
        form = CustomUserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically logs in the user
            return redirect('homepage')  # Redirect to homepage
    else:
        form = CustomUserRegistrationForm()
    
    return render(request, 'sign-up.html', {'form': form})