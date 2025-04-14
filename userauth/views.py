from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserRegistrationForm, CustomUserEditForm
from django.views.decorators.cache import never_cache

# Register view (no login required)
@never_cache
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
@never_cache
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
@never_cache
def logout_view(request):
    logout(request)
    return redirect('homepage') # changed redirect to homepage

# Settings view — requires login
@login_required(login_url='/auth/login/')
@never_cache
def settings_view(request):
    if request.method == 'POST':
        if 'update' in request.POST:
            form = CustomUserEditForm(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                return redirect('homepage')
        
        elif 'delete' in request.POST:
            request.user.delete()
            logout(request)
            return redirect('homepage')
    else:
        form = CustomUserEditForm(instance=request.user)

    return render(request, 'settings.html', {'form': form})

# Delete account view
@login_required
@never_cache
def delete_account_view(request):
    if request.method == 'POST':
        request.user.delete()
        logout(request)
        return redirect('login')
    return redirect('settings')
