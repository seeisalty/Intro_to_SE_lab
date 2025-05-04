from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

# Registration form for user
class CustomUserRegistrationForm(UserCreationForm):
    role = forms.ChoiceField(choices=[('buyer', 'Buyer'), ('seller', 'Seller')])

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'role']


class CustomUserEditForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name']  # removed Role field as sellers are not supposed to be able to shop only sell
                                                                    # if your role was buyer and you added things to cart, your cart would still have those items
                                                                    # if you switched your role to seller thus enabling sellers to buy items
        
