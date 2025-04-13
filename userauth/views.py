from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserRegistrationForm, CustomUserEditForm

# Register view (no login required)
def register_view(request):
    if request.method == 'POST':
        form = CustomUserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in
            return redirect('homepage')  # Redirect to the homepage after successful sign-up
    else:
        form = CustomUserRegistrationForm()
    
    return render(request, 'sign-up.html', {'form': form})

# Login view
def login_view(request):
    if request.user.is_authenticated:
        return redirect('homepage')  # redirect if already logged in

    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('homepage')
        return render(request, 'login.html', {'form': form, 'error': 'Invalid credentials'})

    return render(request, 'login.html', {'form': form})

# Logout view
def logout_view(request):
    logout(request)
    return redirect('login')

# Settings view — requires login
@login_required(login_url='/auth/login/')
def settings_view(request):
    if request.method == 'POST':
        form = CustomUserEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('settings')
    else:
        form = CustomUserEditForm(instance=request.user)

    return render(request, 'settings.html', {'form': form})