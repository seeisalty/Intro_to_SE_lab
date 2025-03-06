from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

# Registration form for user
class CustomUserRegistrationForm(UserCreationForm):
    role = forms.ChoiceField(choices=[('buyer', 'Buyer'), ('seller', 'Seller')])

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'role']